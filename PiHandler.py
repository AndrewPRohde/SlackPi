from time import sleep
from datetime import datetime
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

#LCD Reference
#https://www.electroniclinic.com/raspberry-pi-16x2-lcd-i2c-interfacing-and-python-programming/
#https://github.com/sterlingbeason/LCD-1602-I2C

lcd = LCD()
def safe_exit(signum, frame):
    exit(1)

