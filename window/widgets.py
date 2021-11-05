from PyQt5 import QtWidgets
from PyQt5.Qt import *


class TimeWidget(QLabel):

    def __init__(self, frame, width, height):
        super(TimeWidget, self).__init__(frame)
        time_shadow_effect = QGraphicsDropShadowEffect(self)
        time_shadow_effect.setOffset(0, 0)
        time_shadow_effect.setColor(QColor("BLACK"))
        time_shadow_effect.setBlurRadius(50)
        self.setStyleSheet("color: rgba(255,255,255,0.7); "
                           "background-color: transparent; "
                           "text-align: middle;"
                           "font-size: 70px;")
        self.setGraphicsEffect(time_shadow_effect)
        self.setFixedSize(width, height)
        self.setText("18:18:18")
