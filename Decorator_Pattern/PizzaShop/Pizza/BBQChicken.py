from System_Design.Decorator_Pattern.PizzaShop.Pizza.Pizza import Pizza


class BBQChicken(Pizza):
    def getDescription(self):
        return "BBQChicken"

    def getCost(self):
        return 200
