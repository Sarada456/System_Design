from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza
from System_Design.Decorator_Pattern.PizzaShop.PizzaToppings.PizzaTopping import PizzaTopping


class Paneer(PizzaTopping):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription() + " + Paneer"

    def getCost(self):
        return self.pizza.getCost() + 60
