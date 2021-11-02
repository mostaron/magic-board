from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.imgLabel = QLabel(self)
        desktop = QtWidgets.QApplication.desktop()
        self.width = desktop.width()
        self.height = desktop.height()
        print("屏幕宽{},高{}".format(self.width, self.height))
        self.init_ui()
        self.exit_count = 0

    def init_ui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.imgLabel.setFixedSize(self.width, self.height)
        self.imgLabel.move(0, 0)
        self.imgLabel.setStyleSheet("QLabel{background: Black;}")
        img = QtGui.QPixmap("/Users/neil/103976/PIC-总数统计.png").scaled(self.width, self.height)
        self.imgLabel.setPixmap(img)
        self.move(0, 0)
        self.showNormal()

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Escape:
            if self.exit_count < 2:
                self.exit_count += 1
                self.imgLabel.clear()
            else:
                sys.exit()


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
