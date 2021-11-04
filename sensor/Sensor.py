try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO
import time

# 声音感应器OUT口连接的GPIO
# 光感
SENSOR = 11
# 声感
SENSOR2 = 19

LIGHT_STATUS = 0

DARK_STATUS = 1


class Sensors:

    def __init__(self, sound_handler, light_handler):

        print("init sensor")

        GPIO.setmode(GPIO.BOARD)

        # 指定GPIO4（声音感应器的OUT口连接的GPIO口）的模式为输入模式
        # 默认拉高到高电平，低电平表示OUT口有输出
        GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(SENSOR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.sound_handler = sound_handler
        self.light_handler = light_handler

        # 监听光感
        GPIO.add_event_detect(SENSOR, GPIO.BOTH, self.callback_light, bouncetime=300)
        # 监听声控
        GPIO.add_event_detect(SENSOR2, GPIO.BOTH, self.callback_sound, bouncetime=300)

    def callback_light(self, channel):
        # 检测声音感应器是否输出低电平，若是低电平，表示声音被检测到，点亮或关闭LED
        print('light', channel, GPIO.input(SENSOR), GPIO.input(SENSOR2))
        self.light_handler(GPIO.input(SENSOR))

    def callback_sound(self, channel):
        # 检测声音感应器是否输出低电平，若是低电平，表示声音被检测到，点亮或关闭LED
        print('sound', channel, GPIO.input(SENSOR), GPIO.input(SENSOR2))
        self.sound_handler(GPIO.input(SENSOR))
