# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Sat May 18 06:07:02 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(740, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        Preferences.setMinimumSize(QtCore.QSize(740, 400))
        Preferences.setMaximumSize(QtCore.QSize(740, 400))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Preferences)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Preferences)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabAuth = QtGui.QWidget()
        self.tabAuth.setObjectName(_fromUtf8("tabAuth"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabAuth)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBoxMarket = QtGui.QGroupBox(self.tabAuth)
        self.groupBoxMarket.setEnabled(True)
        self.groupBoxMarket.setFlat(True)
        self.groupBoxMarket.setObjectName(_fromUtf8("groupBoxMarket"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxMarket)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditPassword = QtGui.QLineEdit(self.groupBoxMarket)
        self.lineEditPassword.setEnabled(True)
        self.lineEditPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.gridLayout.addWidget(self.lineEditPassword, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxMarket)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.labelPassword = QtGui.QLabel(self.groupBoxMarket)
        self.labelPassword.setWordWrap(True)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.gridLayout.addWidget(self.labelPassword, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBoxMarket)
        self.groupBoxApplication = QtGui.QGroupBox(self.tabAuth)
        self.groupBoxApplication.setFlat(True)
        self.groupBoxApplication.setObjectName(_fromUtf8("groupBoxApplication"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxApplication)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBoxApplication)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBoxApplication)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditSecret = QtGui.QLineEdit(self.groupBoxApplication)
        self.lineEditSecret.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEditSecret.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEditSecret.setObjectName(_fromUtf8("lineEditSecret"))
        self.gridLayout_2.addWidget(self.lineEditSecret, 3, 1, 1, 1)
        self.lineEditKey = QtGui.QLineEdit(self.groupBoxApplication)
        self.lineEditKey.setObjectName(_fromUtf8("lineEditKey"))
        self.gridLayout_2.addWidget(self.lineEditKey, 2, 1, 1, 1)
        self.labelKeySecret = QtGui.QLabel(self.groupBoxApplication)
        self.labelKeySecret.setWordWrap(True)
        self.labelKeySecret.setObjectName(_fromUtf8("labelKeySecret"))
        self.gridLayout_2.addWidget(self.labelKeySecret, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBoxApplication)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tabAuth, _fromUtf8(""))
        self.tabVarious = QtGui.QWidget()
        self.tabVarious.setObjectName(_fromUtf8("tabVarious"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabVarious)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBoxCurrency = QtGui.QGroupBox(self.tabVarious)
        self.groupBoxCurrency.setEnabled(True)
        self.groupBoxCurrency.setFlat(True)
        self.groupBoxCurrency.setObjectName(_fromUtf8("groupBoxCurrency"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxCurrency)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_Fiat = QtGui.QLabel(self.groupBoxCurrency)
        self.label_Fiat.setMinimumSize(QtCore.QSize(100, 0))
        self.label_Fiat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Fiat.setObjectName(_fromUtf8("label_Fiat"))
        self.gridLayout_3.addWidget(self.label_Fiat, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.labelCurrencyboxDescription = QtGui.QLabel(self.groupBoxCurrency)
        self.labelCurrencyboxDescription.setTextFormat(QtCore.Qt.AutoText)
        self.labelCurrencyboxDescription.setWordWrap(True)
        self.labelCurrencyboxDescription.setObjectName(_fromUtf8("labelCurrencyboxDescription"))
        self.gridLayout_3.addWidget(self.labelCurrencyboxDescription, 0, 1, 1, 2)
        self.comboBoxCurrencyFiat = QtGui.QComboBox(self.groupBoxCurrency)
        self.comboBoxCurrencyFiat.setEditable(False)
        self.comboBoxCurrencyFiat.setMinimumContentsLength(3)
        self.comboBoxCurrencyFiat.setObjectName(_fromUtf8("comboBoxCurrencyFiat"))
        self.gridLayout_3.addWidget(self.comboBoxCurrencyFiat, 1, 1, 1, 1)
        self.comboBoxCurrencyTarget = QtGui.QComboBox(self.groupBoxCurrency)
        self.comboBoxCurrencyTarget.setEditable(False)
        self.comboBoxCurrencyTarget.setMinimumContentsLength(3)
        self.comboBoxCurrencyTarget.setObjectName(_fromUtf8("comboBoxCurrencyTarget"))
        self.gridLayout_3.addWidget(self.comboBoxCurrencyTarget, 2, 1, 1, 1)
        self.label_Target = QtGui.QLabel(self.groupBoxCurrency)
        self.label_Target.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Target.setObjectName(_fromUtf8("label_Target"))
        self.gridLayout_3.addWidget(self.label_Target, 2, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBoxCurrency)
        spacerItem2 = QtGui.QSpacerItem(20, 164, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.setStretch(1, 1)
        self.tabWidget.addTab(self.tabVarious, _fromUtf8(""))
        self.tabVisual = QtGui.QWidget()
        self.tabVisual.setObjectName(_fromUtf8("tabVisual"))
        self.formLayoutWidget = QtGui.QWidget(self.tabVisual)
        self.formLayoutWidget.setGeometry(QtCore.QRect(3, 6, 712, 316))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.doubleSpinBoxGROUPORDERS = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxGROUPORDERS.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxGROUPORDERS.setSizePolicy(sizePolicy)
        self.doubleSpinBoxGROUPORDERS.setMinimumSize(QtCore.QSize(100, 0))
        self.doubleSpinBoxGROUPORDERS.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBoxGROUPORDERS.setDecimals(5)
        self.doubleSpinBoxGROUPORDERS.setMaximum(99999.0)
        self.doubleSpinBoxGROUPORDERS.setSingleStep(0.1)
        self.doubleSpinBoxGROUPORDERS.setObjectName(_fromUtf8("doubleSpinBoxGROUPORDERS"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxGROUPORDERS)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.tabWidget.addTab(self.tabVisual, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelStatus = QtGui.QLabel(Preferences)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.horizontalLayout.addWidget(self.labelStatus)
        self.buttonBox = QtGui.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Preferences.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.lineEditPassword, self.lineEditKey)
        Preferences.setTabOrder(self.lineEditKey, self.lineEditSecret)
        Preferences.setTabOrder(self.lineEditSecret, self.buttonBox)
        Preferences.setTabOrder(self.buttonBox, self.tabWidget)
        Preferences.setTabOrder(self.tabWidget, self.comboBoxCurrencyFiat)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(_translate("Preferences", "Preferences", None))
        self.groupBoxMarket.setTitle(_translate("Preferences", "Application", None))
        self.lineEditPassword.setToolTip(_translate("Preferences", "Application password", None))
        self.lineEditPassword.setPlaceholderText(_translate("Preferences", "Password", None))
        self.label_2.setText(_translate("Preferences", "Password:", None))
        self.labelPassword.setText(_translate("Preferences", "Set an application-wide password to protect account-related functionalities against misuse.", None))
        self.groupBoxApplication.setTitle(_translate("Preferences", "Market", None))
        self.label_3.setText(_translate("Preferences", "Key:", None))
        self.label_4.setText(_translate("Preferences", "Secret:", None))
        self.lineEditSecret.setToolTip(_translate("Preferences", "Insert your MtGox secret here", None))
        self.lineEditSecret.setPlaceholderText(_translate("Preferences", "Secret", None))
        self.lineEditKey.setToolTip(_translate("Preferences", "Insert your MtGox key here", None))
        self.lineEditKey.setPlaceholderText(_translate("Preferences", "Key", None))
        self.labelKeySecret.setText(_translate("Preferences", "Insert your market\'s (e.g. MtGox) API key here. If you don\'t have an API key yet, you should be able to generate one on your market\'s website.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAuth), _translate("Preferences", "Authentication", None))
        self.groupBoxCurrency.setTitle(_translate("Preferences", "Currency", None))
        self.label_Fiat.setText(_translate("Preferences", "Fiat:", None))
        self.labelCurrencyboxDescription.setText(_translate("Preferences", "Select your fiat currency, and the target currency you would like to trade:", None))
        self.label_Target.setText(_translate("Preferences", "Target:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVarious), _translate("Preferences", "Various Settings", None))
        self.label.setText(_translate("Preferences", "Combine Orders under: ", None))
        self.label_5.setText(_translate("Preferences", "Preferences:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVisual), _translate("Preferences", "Visual / Layout", None))

