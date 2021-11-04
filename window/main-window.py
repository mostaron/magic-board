import os.path

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
import sys, time

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)

from sensor.Sensor import *


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
        # self.imgLabel.setStyleSheet("QLabel{background: White;}")
        # img = QtGui.QPixmap("/Users/neil/103976/PIC-总数统计.png").scaled(self.width, self.height)
        # self.imgLabel.setPixmap(img)
        self.move(0, 0)
        Sensors(sound_handler=self.sound_handler, light_handler=self.light_handler)
        self.showNormal()

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Escape:
            if self.exit_count < 2:
                self.exit_count += 1
                self.imgLabel.clear()
            else:
                sys.exit()

    def sound_handler(self, light_status):
        """
        处理声音事件
        :param light_status:
        :return:
        """
        if light_status == LIGHT_STATUS:
            self.imgLabel.setStyleSheet("QLabel{background: Green;}")
        else:
            self.imgLabel.setStyleSheet("QLabel{background: RED;}")

        time.sleep(10)
        self.light_handler(light_status)

    def light_handler(self, light_status):
        """
        处理光线事件
        :param light_status:
        :return:
        """
        if light_status == LIGHT_STATUS:
            self.imgLabel.setStyleSheet("QLabel{background: Black;}")
        else:
            self.imgLabel.setStyleSheet("QLabel{background: White;}")


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
