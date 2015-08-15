import os


class MacSystemEvent:

    def __init__(self):
        pass

    def pressButton(self, key, using):

        if key in [123, 124, 125, 126]:
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
