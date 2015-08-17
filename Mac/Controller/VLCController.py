import Mac.Driver.OsXSystemDriver


class VLCController:

    appName = 'VLC'

    def handle(self, strCode):
        driver = Mac.Driver.OsXSystemDriver.OsXSystemDriver()

        if strCode == 'OK':
            driver.pressButton('p', 'using {command down}')
        elif strCode == 0:
            driver.pressButton('q', 'using {command down}')
        elif strCode == '#':
            driver.pressButton('f', 'using {command down, control down}')
        elif strCode == 'ARR_UP':
            driver.pressButton(driver.ARROW_UP_CODE, 'using {command down}')
        elif strCode == 'ARR_DOWN':
            driver.pressButton(driver.ARROW_DOWN_CODE, 'using {command down}')
        elif strCode == 'ARR_LEFT':
            driver.pressButton(driver.ARROW_LEFT_CODE, 'using {command down}')
        elif strCode == 'ARR_RIGHT':
            driver.pressButton(driver.ARROW_RIGHT_CODE, 'using {command down}')