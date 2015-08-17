import subprocess
import os


class OsXSystemDriver:
    debug = False

    ARROW_LEFT_CODE = 123
    ARROW_RIGHT_CODE = 124
    ARROW_DOWN_CODE = 125
    ARROW_UP_CODE = 126

    def __init__(self, debug=False):
        self.debug = debug

    def pressButton(self, key, using):
        if key in [self.ARROW_LEFT_CODE, self.ARROW_RIGHT_CODE, self.ARROW_DOWN_CODE, self.ARROW_UP_CODE]:
            cmd = """
                osascript -e '
                    tell application "System Events"
                        key code """ + str(key) + """ """ + using + """
                    end tell
                '
            """
        else:
            cmd = """
                osascript -e '
                    tell application "System Events" to keystroke \"""" + key + """\" """ + using + """
                '
            """

        if self.debug:
            print(cmd)

        os.system(cmd)

    def openApp(self, app_id):
        cmd = """
            osascript -e '
                tell application \"""" + app_id + """\"
                    activate
                end tell
            '
        """
        os.system(cmd)

    def getActiveAPP(self):
        cmd = """
            tell application "System Events"
                set activeApp to name of application processes whose frontmost is true
            end tell
        """
        appName = subprocess.check_output(['osascript', '-e', cmd])
        return appName.decode('UTF-8').rstrip()