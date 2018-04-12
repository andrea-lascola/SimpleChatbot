
class log(object):

    @staticmethod
    def log(msg):
        print(msg)

    @staticmethod
    def info(msg):
        log.log(msg)
