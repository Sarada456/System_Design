from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza
from System_Design.Decorator_Pattern.PizzaShop.PizzaToppings.PizzaTopping import PizzaTopping


class Olive(PizzaTopping):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def getDescription(self):
        return self.pizza.getDescription() + " + Olive"

    def getCost(self):
        return self.pizza.getCost() + 20
