from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def responder(self, mensaje):
        pass