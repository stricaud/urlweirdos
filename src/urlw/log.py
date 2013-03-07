import time

class UrlwLog:
    def __init__(self, filename_or_arg, filename=None):
        if filename == None:
            self.filename = "urlweirdos.log"
        else:
            self.filename = filename

        self.filename_or_arg = filename_or_arg

    def open(self):
        self.logfile = open(self.filename, 'a')

    def close(self):
        self.logfile.close()

    def custom_log(self, message):
        str_time = time.ctime()
        self.logfile.write("[%s]\t[%s]\t%s\n" % (str_time, self.filename_or_arg, message))

    def alert_log(self, plugin, message, url):
        str_time = time.ctime()
        self.logfile.write("[%s]\t[%s]\t[%s]\t%s\ton URL: %s\n" % (str_time, self.filename_or_arg, plugin, message, url))

