from collections import deque
from abc import ABCMeta, abstractmethod


class Command(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class Switch:

    def __init__(self):
        self._history = deque()

    @property
    def history(self):
        return self._history

    def execute(self, command):
        self._history.appendleft(command)
        command.execute()

class Light:
    def turn_on(self):
        print("Light is turned on")
    
    def turn_off(self):
        print("Light is turned off")


class TurnOffCommand(Command):

    def __init__(self, light):
        self.light =  light

    def execute(self):
        self.light.turn_off()



class TurnOnCommand(Command):

    def __init__(self, light):
        self.light =  light

    def execute(self):
        self.light.turn_on()
            
lamp = Light()
switch_on = TurnOnCommand(lamp)
switch_off = TurnOffCommand(lamp)
my_switch = Switch()
my_switch.execute(switch_on)
my_switch.execute(switch_off)


