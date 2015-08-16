from MacSystemEvent import MacSystemEvent


class KeyPressHandler:

    systemEventManager = MacSystemEvent()

    def init(self, systemEventManager):
        self.systemEventManager = systemEventManager

    def handle(self, keyName):

        return self.systemEventManager.getActiveAPP()
        """
        if keyName == 'OK':
            self.systemEventManager.pressButton(125, 'using {command down}')
        elif keyName == '*':
            self.systemEventManager.openApp('Finder')
        elif keyName == 'ARR_DOWN':
            self.systemEventManager.pressButton(125, '')
        elif keyName == 'ARR_UP':
            self.systemEventManager.pressButton(126, '')
        elif keyName == 'ARR_LEFT':
            self.systemEventManager.pressButton(123, 'using {control down}')
        elif keyName == 'ARR_RIGHT':
            self.systemEventManager.pressButton(124, 'using {control down}')
        elif keyName == 0:
            self.systemEventManager.pressButton('q', 'using {command down}')
        elif keyName == '#':
            self.systemEventManager.pressButton('f', 'using {command down, control down}')
        """