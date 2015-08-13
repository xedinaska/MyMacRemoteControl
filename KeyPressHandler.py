from MacSystemEvent import MacSystemEvent


class KeyPressHandler:

    systemEventManager = MacSystemEvent()

    def init(self, systemEventManager):
        self.systemEventManager = systemEventManager

    def handle(self, keyName):

        if keyName == 'OK':
            self.systemEventManager.openApp('VLC')
            self.systemEventManager.pressButton('f', 'command down')
        elif keyName == '*':
            self.systemEventManager.openApp('Finder')
        elif keyName == 'ARR_DOWN':
            self.systemEventManager.pressButton(125, '')
        elif keyName == 'ARR_UP':
            self.systemEventManager.pressButton(126, '')
        elif keyName == 'ARR_LEFT':
            self.systemEventManager.pressButton(123, 'control down')
        elif keyName == 'ARR_RIGHT':
            self.systemEventManager.pressButton(124, 'control down')