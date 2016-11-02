
class TrackerException(Exception):
    """
       Base Class for all Tracker related Exception

       Message = Message Regarding Exception
       data = Data which causes the Exception
       mode = Where the exception occurs
    """

    mode = None

    def __init__(self, message, data):
        self.messsage = message
        self.data = data

    def __repr__(self):
        return "<%s>%s"%(self.__class__.__name__, self.message)

    def __str__(self):
        return self.__repr__()


class TrackerRequestException(TrackerException):
    mode = 'request'


class TrackerResponseException(TrackerException):
    mode = 'response'