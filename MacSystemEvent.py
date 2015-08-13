import os


class MacSystemEvent:

    def __init__(self):
        pass

    def pressButton(self, key, using):

        if key in [123, 124, 125, 126]:
            key_string = 'key code ' + str(key) + ''
        else:
            key_string = "to keystroke \"" + key + "\""

        if using != '':
            cmd = """
                osascript -e '
                    tell application "System Events"
                        """ + key_string + """ using {""" + using + """}
                    end tell
                '
            """
        else:
            cmd = """
                osascript -e '
                    tell application "System Events"
                        """ + key_string + """
                    end tell
                '
            """
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
