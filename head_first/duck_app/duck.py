from abc import ABCMeta, abstractmethod

# abstract methods

class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(metaclass = ABCMeta):

    @abstractmethod
    def quack(self):
        pass



class FlyWithWings(FlyBehavior):
    def fly(self):
            print("Fly with Wings behaviour")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly")

class MuteQuack(QuackBehavior):

    def quack(self):
        print("I can't Quack")


class SpeakQuack(QuackBehavior):

    def quack(self):
        print("Quack Quack Quack Quack yes i can")


class Squeak(QuackBehavior):

    def quack(self):
        print("Squeak Squeak Squeak Squeak")



class Duck:
    flyBehavior = None
    quackBehavior = None
    def __init__(self, flyBehavior, quackBehavior):
        self.flyBehavior = flyBehavior()
        self.quackBehavior = quackBehavior()
    def PerformFly(self):
        self.flyBehavior.fly()

    def PerformQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("all ducks can be swim")





class MallarDuck(Duck):

    def __init__(self, flyBehavior, quackBehavior):
        super(MallarDuck,self).__init__(flyBehavior, quackBehavior)
        

class NormalDuck(Duck):
    def __init__(self, flyBehavior, quackBehavior):
        super(NormalDuck,self).__init__(flyBehavior, quackBehavior)



obj = MallarDuck(FlyNoWay, MuteQuack)
obj.PerformQuack()
obj.PerformFly()

obj2 = NormalDuck(FlyWithWings, SpeakQuack)
obj2.PerformQuack()
obj2.PerformFly()


# obj = MuteQuack()
# obj.quack()

# obj = FlyNoWay()
# obj.fly()