import abc

class AbsAlert(metaclass=abc.ABCMeta):
    def __init__(self):
        self._title = ""
        self._message = ""

    @abc.abstractmethod
    def execute(self):
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    #
    # @abc.abstractproperty
    # def _title_setter(self, value):
    #     pass
    #
    # @abc.abstractproperty
    # def _message_setter(self, value):
    #     pass
    #
    #
