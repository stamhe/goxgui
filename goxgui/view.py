import utilities
import time
import logging

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QTextCursor
from ui.main_window_ import Ui_MainWindow
from model import ModelAsk,ModelBid,ModelOwns,ModelStops
from PyQt4 import QtGui
from goxapi import Timer

class View(QMainWindow):
    '''
    Represents the combined view / control.
    '''

    # how the application-proposed bid will differ from the selected bid
    ADD_TO_BID = 1000

    # how the application-proposed ask will differ from the selected ask
    SUB_FROM_ASK = 1000

    def __init__(self, preferences, market):

        QMainWindow.__init__(self)

        self.preferences = preferences
        self.market = market

        # set up main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # improve ui on mac
        if utilities.platform_is_mac():
            self.adjust_for_mac()

        # connect market signals to our logic
        self.market.signal_log.connect(self.slot_log)
        self.market.signal_wallet.connect(self.display_wallet)
        self.market.signal_orderlag.connect(self.display_orderlag)
        self.market.signal_userorder.connect(self.display_userorder)
        self.market.signal_ticker.connect(self.update_titlebar)

        # connect ui signals to our logic
        self.ui.pushButtonGo.released.connect(self.execute_trade)
        self.ui.tableAsk.clicked.connect(self.update_edit_from_ask_book)
        self.ui.tableBid.clicked.connect(self.update_edit_from_bid_book)
        self.ui.pushButtonCancel.released.connect(self.cancel_order)       
        #enable clicking of OrderID links in the Trading textBrowser
        self.ui.textBrowserStatus.anchorClicked.connect(self.order_selected)
        self.ui.pushButtonWalletA.released.connect(self.set_trade_size_from_wallet)
        self.ui.pushButtonWalletB.released.connect(self.set_trade_total_from_wallet)
        self.ui.pushButtonSize.released.connect(self.recalculate_size)
        self.ui.pushButtonPrice.released.connect(self.update_edit_on_button)
        self.ui.pushButtonTotal.released.connect(self.recalculate_total)
        self.ui.actionPreferences_2.triggered.connect(self.show_preferences)

        # initialize and connect bid / ask table models
        self.modelAsk = ModelAsk(self, self.market)
        self.ui.tableAsk.setModel(self.modelAsk)
        self.modelBid = ModelBid(self, self.market)
        self.ui.tableBid.setModel(self.modelBid)

        # associate log channels with their check boxes
        self.logchannels = [
            [self.ui.checkBoxLogTicker, 'tick'],
            [self.ui.checkBoxLogTrade, 'trade'],
            [self.ui.checkBoxLogDepth, 'depth'],
        ]
 
        #User Orders TAB
        self.modelOwns = ModelOwns(self, self.market)
        self.ui.tableUserOrders.setModel(self.modelOwns)
        self.ui.tableUserOrders.resizeColumnsToContents()
        self.ui.tableUserOrders.clicked.connect(self.userorder_selected)

        # activate market
        self.market.start()
      
        #create the stop orders TAB.
        self.modelStops = ModelStops(self, self.market)
        self.ui.tableStopOrders.setModel(self.modelStops)
        self.ui.tableStopOrders.resizeColumnsToContents()

        #add stop orders into the stop database
        self.ui.pushButton1StopAdd.released.connect(self.add_stopOrder)
        #on click, put Stop Order ID into the cancel button box.
        self.ui.tableStopOrders.clicked.connect(self.stopOrder_selected)
        #remove a stop order
        self.ui.pushButtonStopRemove.released.connect(self.remove_stopOrder)
        #activate the stop loss bot with the checkbox.
        self.ui.checkBoxActivateStopLossBot.clicked.connect(self.stopbot_act_deact)
        
        #for stuff in the Ticker TAB
        self.ui.pushButtonRefreshTicker.released.connect(self.refresh_and_display_ticker)
        self.ui.checkBoxAutoRefreshTicker.clicked.connect(self.autorefresh_ticker_selected)

        #populate the ticker tab fields.
        self.display_ticker()
        
        # show main window
        self.adjustSize()
        self.show()
        self.raise_()

    def adjust_for_mac(self):
        '''
        Fixes some stuff that looks good on windows but bad on mac.
        '''
        # the default fixed font is unreadable on mac, so replace it
        font = QtGui.QFont('Monaco', 11)
        self.ui.tableAsk.setFont(font)
        self.ui.tableBid.setFont(font)
        self.ui.textBrowserLog.setFont(font)
        self.ui.textBrowserStatus.setFont(font)
        self.ui.lineEditOrder.setFont(font)
        self.ui.doubleSpinBoxBtc.setFont(font)
        self.ui.doubleSpinBoxPrice.setFont(font)
        self.ui.doubleSpinBoxTotal.setFont(font)

        # the space between application title bar and
        # the ui elements is too small on mac
        margins = self.ui.widgetMain.layout().contentsMargins()
        margins.setTop(24)
        self.ui.widgetMain.layout().setContentsMargins(margins)

    def show_preferences(self):

        result = self.preferences.show()
        if result == True:
            self.status_message('Preferences changed, restarting market.')
            self.market.stop()
            self.preferences.apply()
            self.market.start()
            self.status_message('Market restarted successfully.')
        
        
    def display_ticker(self):
        if not self.market.ticker.ticker_fast.get("error"):
            self.ui.lineEdit1Buy.setText("$" + self.market.ticker.buy)
            self.ui.lineEdit2Sell.setText("$" + self.market.ticker.sell)
            self.ui.lineEdit3Last.setText("$" + self.market.ticker.last)
        else:
            self.ui.lineEdit1Buy.setText("Error")
            self.ui.lineEdit2Sell.setText("Error")
            self.ui.lineEdit3Last.setText("Error")

        if not self.market.ticker.ticker2.get("error"):
            self.ui.lineEdit4Volume.setText(self.market.ticker.volumestr)
            self.ui.lineEdit5High.setText("$" + self.market.ticker.high)
            self.ui.lineEdit6Low.setText("$" + self.market.ticker.low)
            self.ui.lineEdit7Avg.setText("$" + self.market.ticker.avg)
            self.ui.lineEdit8VWAP.setText("$" + self.market.ticker.vwap)
        else:
            self.ui.lineEdit4Volume.setText("Error")
            self.ui.lineEdit5High.setText("Error")
            self.ui.lineEdit6Low.setText("Error")
            self.ui.lineEdit7Avg.setText("Error")
            self.ui.lineEdit8VWAP.setText("Error")
            

    def refresh_and_display_ticker(self,dummy_1=None,dummy_2=None):
        self.market.ticker.refresh_both()
        self.display_ticker()
                    
    def autorefresh_ticker_selected(self):
        if self.ui.checkBoxAutoRefreshTicker.isChecked():
            interval = self.ui.spinBoxAutoRefreshTicker.value()
            self.market.ticker_refresh_timer = Timer(interval)
            self.market.ticker_refresh_timer.connect(self.refresh_and_display_ticker)
        else:
            if self.market.ticker_refresh_timer:
                self.market.ticker_refresh_timer.cancel()
        
        
    def add_stopOrder(self):
        size = float(self.ui.lineEdit1StopSize.text())  #read from input boxes
        price = float(self.ui.lineEdit2StopPrice.text())
        self.ui.lineEdit1StopSize.setText('')   #set input boxes to blank again
        self.ui.lineEdit2StopPrice.setText('')
        oid = len(self.market.gox.stopOrders)+1                #set OID number to a human number(OID# is actually just for us humans)
        self.market.gox.stopOrders.append([oid,size,price])    #add order to the list
        self.modelStops.changed()                       #trigger the changed function

    def stopOrder_selected(self, index):
        self.ui.lineEdit3StopID.setText(str(self.modelStops.get(index.row(),0)))        
        
    def remove_stopOrder(self):
        oid = self.ui.lineEdit3StopID.text()    #read OID from the input box
        oid = int(oid)-1                                #change human OID to internal
        self.ui.lineEdit3StopID.setText('')     #set input box to blank
        self.market.gox.stopOrders.remove(self.market.gox.stopOrders[oid])    #remove order from the list
        self.modelStops.changed()                       #trigger the changed function

    def stopbot_act_deact(self):
        if self.ui.checkBoxActivateStopLossBot.isChecked():     #if the checkbox is active
            self.market.gox.stopbot_active = True              #enable stop-loss bot
        else:
            self.market.gox.stopbot_active = False             #or disable it.

    def update_titlebar(self,bid,ask):
        #change the title bar to match any updates from the ticker channel
        try:
            volstring = ", Vol: " + self.market.ticker.volumestr[:-4] + " BTC" #has some strange unicode char in it.
        except:
            volstring = ""
        newtitle = "MtGox Trading UI - Bid: {0}, Ask: {1}{2}".format(bid/1E5,ask/1E5,volstring)
        self.setWindowTitle(QtGui.QApplication.translate("ui", newtitle, None, QtGui.QApplication.UnicodeUTF8))
        
    def get_selected_trade_type(self):
        if self.ui.radioButtonBuy.isChecked():
            return 'BUY'
        else:
            return 'SELL'

    def set_selected_trade_type(self, trade_type):
        if trade_type == 'BUY':
            self.ui.radioButtonBuy.toggle()
        else:
            self.ui.radioButtonSell.toggle()

    def slot_log(self, text):

        logging.info(text)
        text = self.prepend_date(text)

        doOutput = False

        if self.ui.checkBoxLogSystem.isChecked():
            doOutput = True

        for entry in self.logchannels:
            if entry[1] in text:
                doOutput = entry[0].isChecked()

        if doOutput:
            self.ui.textBrowserLog.append(text)

    def prepend_date(self, text):
        millis = int(round(time.time() * 1000)) % 1000
        return '{}.{:0>3} {}'.format(time.strftime('%X'), millis, text)

    def status_message(self, text):
        # call move cursor before append to work around link clicking bug
        # see: https://bugreports.qt-project.org/browse/QTBUG-539
        logging.info(text)
        text = self.prepend_date(text)
        self.ui.textBrowserStatus.moveCursor(QTextCursor.End)
        self.ui.textBrowserStatus.append(text)

    def set_wallet_btc(self, value):
        self.ui.pushButtonWalletA.setEnabled(value > 0)
        self.ui.pushButtonWalletA.setText(
            'BTC: ' + utilities.internal2str(value))

    def set_wallet_usd(self, value):
        self.ui.pushButtonWalletB.setEnabled(value > 0)
        self.ui.pushButtonWalletB.setText(
            'USD: ' + utilities.internal2str(value, 5))

    def get_trade_size(self):
        value = self.ui.doubleSpinBoxBtc.value()
        return utilities.float2internal(value)

    def set_trade_size(self, value):
        value_float = utilities.internal2float(value)
        self.ui.doubleSpinBoxBtc.setValue(value_float)

    def get_trade_price(self):
        value = self.ui.doubleSpinBoxPrice.value()
        return utilities.float2internal(value)

    def set_trade_price(self, value):
        value_float = utilities.internal2float(value)
        self.ui.doubleSpinBoxPrice.setValue(value_float)

    def get_trade_total(self):
        value = self.ui.doubleSpinBoxTotal.value()
        return utilities.float2internal(value)

    def set_trade_total(self, value):
        value_float = utilities.internal2float(value)
        self.ui.doubleSpinBoxTotal.setValue(value_float)

    def get_order_id(self):
        return str(self.ui.lineEditOrder.text())

    def set_order_id(self, text):
        self.ui.lineEditOrder.setText(text)

    def order_selected(self, url):
        self.set_order_id(str(url.toString()))

    def display_wallet(self):

        self.set_wallet_usd(
            utilities.gox2internal(self.market.get_balance('USD'), 'USD'))
        self.set_wallet_btc(
            utilities.gox2internal(self.market.get_balance('BTC'), 'BTC'))

    def set_trade_size_from_wallet(self):
        self.set_trade_size(
            utilities.gox2internal(self.market.get_balance('BTC'), 'BTC'))
        self.set_selected_trade_type('SELL')

    def set_trade_total_from_wallet(self):
        self.set_trade_total(
            utilities.gox2internal(self.market.get_balance('USD'), 'USD'))
        self.set_selected_trade_type('BUY')

    def display_orderlag(self, ms, text):
        self.ui.labelOrderlag.setText('Trading Lag: ' + text)

    def execute_trade(self):

        trade_type = self.get_selected_trade_type()

        size = self.get_trade_size()
        price = self.get_trade_price()
        total = self.get_trade_total()

        trade_name = 'BID' if trade_type == 'BUY' else 'ASK'

        self.status_message('Placing order: {0} {1} BTC at {2} USD (total {3} USD)...'.format(# @IgnorePep8
            trade_name,
            utilities.internal2str(size),
            utilities.internal2str(price, 5),
            utilities.internal2str(total, 5)))

        if trade_type == 'BUY':
            self.market.buy(price, size)
        else:
            self.market.sell(price, size)

    def recalculate_size(self):
        #When the size button is clicked:
        price = self.get_trade_price()
        if price == 0:
            return

        total = self.get_trade_total()
        #divide Total by Price and fill the size edit box in.
        size = utilities.divide_internal(total, price)
        self.set_trade_size(size)

    def recalculate_total(self):
        #When the total button is clicked
        price = self.get_trade_price()
        size = self.get_trade_size()
        #Multiply Price by Size and fill the total edit box in
        total = utilities.multiply_internal(price, size)
        self.set_trade_total(total)

    def display_userorder(self, price, size, order_type, oid, status):

        size = utilities.gox2internal(size, 'BTC')
        price = utilities.gox2internal(price, 'USD')

        size = utilities.internal2str(size)
        price = utilities.internal2str(price,5)

        if order_type == '':
            self.status_message("Order <a href=\"{0}\">{0}</a> {1}.".format(
                oid, status))
            if status == 'removed' and self.get_order_id() == oid:
                self.set_order_id('')
        else:
            self.status_message("{0} size: {1}, price: {2}, oid: <a href=\"{3}\">{3}</a> - {4}".format(# @IgnorePep8
                str.upper(str(order_type)), size, price, oid, status))
            if status == 'post-pending':
                self.set_order_id(oid)
                
    def userorder_selected(self, index):
        mapdict = {"ask":"SELL","bid":"BUY"}
        self.set_selected_trade_type(mapdict[self.modelOwns.get_typ(index.row())])
        self.set_trade_price(self.modelOwns.get_price(index.row()))
        self.set_trade_size(self.modelOwns.get_size(index.row()))
        self.set_order_id(self.modelOwns.get_oid(index.row()))
        
    def cancel_order(self):
        if self.ui.checkBoxCancelAll.isChecked():
            self.market.cancel_by_type()
            self.ui.checkBoxCancelAll.setChecked(False)
        else:
            order_id = self.get_order_id()
            self.status_message(
                "Cancelling order <a href=\"{0}\">{0}</a>...".format(order_id))
            self.market.cancel(order_id)
            
    def update_edit_from_ask_book(self, index):
        #when a order on the ask side is clicked
        #set the radio button to the opposite (buy) 
        self.set_trade_price(self.modelAsk.get_price(index.row()))  #set the price edit box 
        self.set_trade_size(self.modelAsk.get_size(index.row()))    #set the size edit box
        self.set_selected_trade_type('BUY')                        #set the BUY radiobutton
        
    def update_edit_from_bid_book(self, index):
        #when a order on the bids side is clicked 
        #set the radio button to the opposite (sell)
        self.set_trade_price(self.modelBid.get_price(index.row()))  #set the price edit box
        self.set_trade_size(self.modelBid.get_size(index.row()))    #set the size edit box
        self.set_selected_trade_type('SELL')                         #set the SELL radiobutton
       
    def update_edit_on_button(self):
        #When Price button is clicked, fill in the edit boxes, 
        trade_type = self.get_selected_trade_type()
        #depending on which radiobutton "Buy" or "Sell" is selected at the time,
        #get the OPPOSITE side's current best price and the corresponding size 
        mapdict = {"SELL":self.modelBid,"BUY":self.modelAsk}
        self.set_trade_price(mapdict[trade_type].get_price(0))
        self.set_trade_size(mapdict[trade_type].get_size(0))        
        #so you can fulfill that person's current best offer just by clicking Go.
        #(This functionality is something I want, and I can understand it being confusing having it on this button)
        #because the size button behaves normally the original way still.
        #similarly confusing having it map to the opposite side (but necessary)
        #

    def stop(self):
        self.market.stop()        
