from abc import ABC, abstractmethod
from ..Pizza.Pizza import Pizza


class PizzaTopping(Pizza, ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass

    # Extra function related to Toppings can be added here
    # @abstractmethod
    # def quantity(self):
    #     pass
