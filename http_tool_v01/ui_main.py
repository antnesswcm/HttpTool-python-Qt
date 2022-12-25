# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 574)
        MainWindow.setMinimumSize(QSize(500, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.requests_mode = QComboBox(self.centralwidget)
        self.requests_mode.addItem("")
        self.requests_mode.addItem("")
        self.requests_mode.setObjectName(u"requests_mode")

        self.horizontalLayout_2.addWidget(self.requests_mode)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 0))
        self.pushButton.setMaximumSize(QSize(50, 100))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.url_input = QLineEdit(self.centralwidget)
        self.url_input.setObjectName(u"url_input")

        self.horizontalLayout_2.addWidget(self.url_input)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.start_button)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.clear_button)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.requests_head = QTextEdit(self.centralwidget)
        self.requests_head.setObjectName(u"requests_head")

        self.verticalLayout.addWidget(self.requests_head)

        self.response_head = QTextEdit(self.centralwidget)
        self.response_head.setObjectName(u"response_head")
        self.response_head.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.response_head)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.response_body = QPlainTextEdit(self.centralwidget)
        self.response_body.setObjectName(u"response_body")

        self.horizontalLayout.addWidget(self.response_body)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.requests_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.requests_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"HTTPS", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.response_body.setPlainText("")
    # retranslateUi

