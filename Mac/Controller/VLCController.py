import Mac.Driver.OsXSystemDriver


class VLCController:

    appName = 'VLC'

    def handle(self, strCode):
        driver = Mac.Driver.OsXSystemDriver.OsXSystemDriver()

        if strCode == 0:
            driver.pressButton('q', 'using {command down}')
        elif strCode == '#':
            driver.pressButton('f', 'using {command down, control down}')