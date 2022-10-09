from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass
