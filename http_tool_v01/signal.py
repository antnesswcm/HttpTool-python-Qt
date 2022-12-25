#   -*- coding = utf8 -*-
from PySide6.QtCore import Signal, QObject


class MySignal(QObject):
    toggleButtonStatus = Signal(object)
    setQTextEdit_text = Signal(object, str)
    setQPlainTextEdit_text = Signal(object, str)


mySignal = MySignal()
