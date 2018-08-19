from quack import QuackBehavior

class MuteQuack(QuackBehavior):

    def quack(self):
        print("I can't Quack")
