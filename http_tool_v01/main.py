#   -*- coding = utf8 -*-
import sys
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from signal import mySignal

from spider_tool import Crawler


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setObjectName(u"MainWindow")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()
        self.crawler = Crawler(name='crawler')

    def bind(self):
        self.ui.start_button.clicked.connect(self.start)
        self.ui.clear_button.clicked.connect(self.clear)
        mySignal.toggleButtonStatus.connect(self.toggleButtonStatus)
        mySignal.setQTextEdit_text.connect(self.setQTextEdit_text)
        mySignal.setQPlainTextEdit_text.connect(self.setQPlainTextEdit_text)

    @staticmethod
    def setQTextEdit_text(QTextEditObject: object, text: str):
        QTextEditObject.setText(text)

    @staticmethod
    def setQPlainTextEdit_text(QPlainTextEditObject: object, text: str):
        QPlainTextEditObject.setPlainText(text)

    @staticmethod
    def toggleButtonStatus(ButtonObject: object):
        ButtonObject.setEnabled(False if ButtonObject.isEnabled() else True)

    def start(self):
        mySignal.toggleButtonStatus.emit(self.ui.start_button)
        self.clear()

        def innerFunc():
            requests_mode = self.ui.requests_mode.currentIndex()
            url = self.ui.url_input.text()
            print(url)
            if requests_mode == 0:
                _id = self.crawler.get(url)
                mySignal.setQTextEdit_text.emit(self.ui.response_head, self.crawler.view_resHeader(_id))
                mySignal.setQTextEdit_text.emit(self.ui.requests_head, self.crawler.view_reqHeader(_id))
                mySignal.setQPlainTextEdit_text.emit(self.ui.response_body, self.crawler.view_resBody(_id))
            else:
                pass
            mySignal.toggleButtonStatus.emit(self.ui.start_button)

        task = Thread(target=innerFunc)
        task.start()

    def clear(self):
        print("clear")
        self.ui.requests_head.clear()
        self.ui.response_head.clear()
        self.ui.response_body.clear()


if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
