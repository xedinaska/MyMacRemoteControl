import serial
import time
#from KeyPressHandler import KeyPressHandler
from HashCodeReader import HashCodeReader
from OsResolver import OsResolver

port = '/dev/tty.wchusbserial1d1110'
arduinoSerial = serial.Serial(port, 9600, timeout=0)

keyCodesReader = HashCodeReader()
osResolver = OsResolver()

while 1:
    try:
        hashCode = arduinoSerial.readline()
        strCode = keyCodesReader.getKeyName(hashCode)

        applicationsManager = osResolver.getApplicationsManager()
        applicationsManager.handle(strCode)

    except Exception as e:
        print(str(e))

    time.sleep(1)

arduinoSerial.close()