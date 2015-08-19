class HashCodeReader:
    ARR_UP = 'ARR_UP'
    ARR_DOWN = 'ARR_DOWN'
    ARR_LEFT = 'ARR_LEFT'
    ARR_RIGHT = 'ARR_RIGHT'
    OK = 'OK'

    codes = {
        b'FF629D\r\n': ARR_UP,
        b'FFA857\r\n': ARR_DOWN,
        b'FF22DD\r\n': ARR_LEFT,
        b'FFC23D\r\n': ARR_RIGHT,
        b'FF02FD\r\n': OK,
        b'FF6897\r\n': 1,
        b'FF9867\r\n': 2,
        b'FFB04F\r\n': 3,
        b'FF30CF\r\n': 4,
        b'FF18E7\r\n': 5,
        b'FF7A85\r\n': 6,
        b'FF10EF\r\n': 7,
        b'FF38C7\r\n': 8,
        b'FF5AA5\r\n': 9,
        b'FF4AB5\r\n': 0,
        b'FF42BD\r\n': '*',
        b'FF52AD\r\n': '#'
    }

    def getKeyName(self, code):
        return self.codes.get(code)