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
    def __init__(self):
        pass
        
    def PerformFly(self):
        self.flyBehavior.fly()

    def PerformQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print("all ducks can be swim")
    
    def SetFlyingBehaviour(self, flyingBehavior):
        self.flyBehavior = flyingBehavior()
    
    def SetQuackBehaviour(self, quackBehavior):
        self.quackBehavior = quackBehavior()





class MallarDuck(Duck):

    def __init__(self, flyBehavior, quackBehavior):
        self.flyBehavior = flyBehavior()
        self.quackBehavior = quackBehavior()
        # super(MallarDuck,self).__init__(flyBehavior, quackBehavior)
    def SetFlyingBehaviour(self, flyingBehavior):
            return super(MallarDuck, self).SetFlyingBehaviour(flyingBehavior)
    def SetQuackBehaviour(self, quackBehavior):
            return super(MallarDuck, self).SetQuackBehaviour(quackBehavior)

class NormalDuck(Duck):
    def __init__(self, flyBehavior, quackBehavior):
        self.flyBehavior = flyBehavior()
        self.quackBehavior = quackBehavior()
        # super(NormalDuck,self).__init__(flyBehavior, quackBehavior)



# obj = MallarDuck(FlyNoWay, MuteQuack)
# obj.PerformQuack()
# obj.PerformFly()

obj2 = NormalDuck(FlyWithWings, SpeakQuack)
obj2.PerformQuack()
obj2.PerformFly()

obj2.SetFlyingBehaviour(FlyNoWay)
obj2.SetQuackBehaviour(MuteQuack)
print("<============After changing Behavior=============>")
obj2.PerformQuack()
obj2.PerformFly()


# obj = MuteQuack()
# obj.quack()

# obj = FlyNoWay()
# obj.fly()