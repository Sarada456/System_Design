from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza


class Pepperoni(Pizza):
    def getDescription(self):
        return "Pepperoni"

    def getCost(self):
        return 180
