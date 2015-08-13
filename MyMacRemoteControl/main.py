import serial
import time
from KeyPressHandler import KeyPressHandler
from KeyCodesParser import KeyCodesParser

port = '/dev/tty.wchusbserial1d1110'
arduinoSerial = serial.Serial(port, 9600, timeout=0)

keyCodesParser = KeyCodesParser()
handler = KeyPressHandler()

while 1:
    try:
        code = arduinoSerial.readline()
        keyName = keyCodesParser.getKeyName(code)
        handler.handle(keyName)
    except Exception as e:
        print(str(e))

    time.sleep(1)

arduinoSerial.close()