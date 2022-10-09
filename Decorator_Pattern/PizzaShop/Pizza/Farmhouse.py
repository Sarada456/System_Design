from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza


class Farmhouse(Pizza):
    def getDescription(self):
        return "Farmhouse"

    def getCost(self):
        return 150
