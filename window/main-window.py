import os.path

from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import *
import sys
from concurrent.futures import ThreadPoolExecutor

import files.PhotoManage
import widgets

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)

from sensor.Sensor import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # photo
        self.imgLabel = QLabel(self)
        # timeLabel
        self.timeLabel = widgets.TimeWidget(self, 500, 250)
        # desktop = QtWidgets.QApplication.desktop()
        self.width = 1024
        self.height = 600
        print("屏幕宽{},高{}".format(self.width, self.height))

        self.photoThreadPool = ThreadPoolExecutor(max_workers=1)
        self.exit_signal = False;
        self.init_ui()
        self.exit_count = 0

    def init_img_label(self):
        photos = files.PhotoManage.photos
        photo_size = len(photos)
        current_photo = 0
        while True and not self.exit_signal:
            photo = files.PhotoManage.PHOTO_PATH + '/' + photos[current_photo]
            print(photo)
            img = QtGui.QPixmap(photo)
            self.imgLabel.setScaledContents(True)
            self.imgLabel.setPixmap(img)
            time.sleep(5)
            current_photo = (current_photo + 1) % photo_size

    def init_ui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.imgLabel.setFixedSize(self.width, self.height)
        self.imgLabel.move(0, 0)
        self.imgLabel.setStyleSheet("QLabel{background: White;}")
        self.timeLabel.move(0, 0)
        self.timeLabel.raise_()
        self.move(0, 0)
        self.photoThreadPool.submit(self.init_img_label)
        Sensors(sound_handler=self.sound_handler, light_handler=self.light_handler)
        self.showNormal()

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Escape:
            if self.exit_count < 2:
                self.exit_count += 1
                self.imgLabel.clear()
                self.imgLabel.setStyleSheet("QLabel{background: White;}")
            else:
                self.exit_signal = True
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
            self.imgLabel.setStyleSheet("QLabel{background: White;}")
        else:
            self.imgLabel.setStyleSheet("QLabel{background: Black;}")


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
