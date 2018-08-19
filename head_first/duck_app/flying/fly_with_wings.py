from fly import FlyBehavior


class FlyNoWay(FlyBehavior):

    def quack(self):
        print("I can't fly")