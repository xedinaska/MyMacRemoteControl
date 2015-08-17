import Mac.Driver.OsXSystemDriver


class FinderController:

    appName = 'Finder'

    def handle(self, strCode):
        driver = Mac.Driver.OsXSystemDriver.OsXSystemDriver()

        if strCode == 0:
            driver.pressButton('w', 'using {command down}')
        elif strCode == '#':
            driver.pressButton('f', 'using {command down, control down}')
        elif strCode == 'ARR_LEFT':
            driver.pressButton(driver.ARROW_LEFT_CODE, 'using {control down}')
        elif strCode == 'ARR_RIGHT':
            driver.pressButton(driver.ARROW_RIGHT_CODE, 'using {control down}')