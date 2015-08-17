from Mac import MacApplicationsManager
from Windows import WindowsApplicationManager


class OsResolver:

    osXType = 'MAC'
    windowsType = 'WINDOWS'

    def __init__(self):
        pass

    def getApplicationsManager(self):
        osType = self.getOsType()

        if osType == self.osXType:
            return MacApplicationsManager.MacApplicationsManager()
        else:
            return WindowsApplicationManager.WindowsApplicationsManager()

    def getOsType(self):
        return self.osXType