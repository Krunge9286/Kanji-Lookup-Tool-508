import abc
from app.enums import *
from app.kanji import Kanji

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_kanji(self, literal):
        raise NotImplementedError
