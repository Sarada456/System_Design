from System_Design.Decorator_Pattern.PizzaShop.Pizza.BBQChicken import BBQChicken
from System_Design.Decorator_Pattern.PizzaShop.PizzaToppings.Tomato import Tomato
from System_Design.Decorator_Pattern.PizzaShop.PizzaToppings.Cheese import Cheese
from System_Design.Decorator_Pattern.PizzaShop.PizzaToppings.Paneer import Paneer


if __name__ == '__main__':
    pizza = Paneer(Cheese(Tomato(BBQChicken())))
    print(pizza.getCost())
    print(pizza.getDescription())
