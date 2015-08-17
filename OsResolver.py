from Mac import MacApplicationsManager
from Windows import WindowsApplicationManager
from sys import platform as _platform


class OsResolver:

    osXType = 'MAC'
    windowsType = 'WINDOWS'
    linuxType = 'Linux'

    def __init__(self):
        pass

    def getApplicationsManager(self):
        osType = self.getOsType()

        if osType == self.osXType:
            return MacApplicationsManager.MacApplicationsManager()
        else:
            return WindowsApplicationManager.WindowsApplicationsManager()

    def getOsType(self):
        if _platform == "linux" or _platform == "linux2":
            return self.linuxType
        elif _platform == "darwin":
            return self.osXType
        elif _platform == "win32":
            return self.windowsType
