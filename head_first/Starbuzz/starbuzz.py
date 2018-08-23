from abc import ABC, abstractmethod


class Beverage(ABC):
    @property
    def description(self):
        raise NotImplementedError

    def getDescription(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage, ABC):
    @abstractmethod
    def getDescription(self):
        pass

class Expresso(Beverage):
    description = "Expresso"
    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    description = "HouseBlend"
    def cost(self):
        return 0.89

class DarkRoast(Beverage):
    description = "DrakRoast"
    def cost(self):
        return 0.5


class Mocha(CondimentDecorator):
    beverage = None
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return 0.20+self.beverage.cost()


class Whip(CondimentDecorator):
    beverage = None
    def __init__(self,  beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription()+ ", Whip"

    def cost(self):
        return 0.30 + self.cost()



beverage = Expresso()
beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
beverage2 = Mocha(beverage2)
print(beverage2.getDescription())
print("Cost of Bevarge =", beverage.cost())