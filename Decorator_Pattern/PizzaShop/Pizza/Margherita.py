from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza


class Margherita(Pizza):
    def getDescription(self):
        return "Margherita"

    def getCost(self):
        return 200
