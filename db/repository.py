import abc
from model.enums import *
from model.kanji import Kanji

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_kanji(self, literal):
        raise NotImplementedError
