from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class AbstratCar(metaclass = ABCMeta):
    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class Car:
    def drive(self):
        print("Car has been driven")

class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstratCar):

    def __init__(self, driver):
        self.driver = driver
        self.car = Car()
    
    def drive(self):
        if(self.driver.age < 18):
            print("we dont allow you to drive a car driver is too young")
        else:
            self.car.drive()



driver1 = Driver(16)
proxy_obj = ProxyCar(driver1)
proxy_obj.drive()

driver2 = Driver(19)
proxy_obj1 = ProxyCar(driver2)
proxy_obj1.drive()
