import sys

class Singleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if(not cls.instance):
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance
    

class Overloading:

    def __init__(self, value):
        self.value = value

    def __del__(self):
        print("destroy object with value : ",self.value)

    def __str__(self):
        return "String Representation of object : "+str(self.value)
         
    def __cmp__(self, other):
        return other.value == self.value



obj = Overloading(10)
obj1 = Overloading(10)
print("Obj1 and obj2 is {}".format(obj.__cmp__(obj1)))
print(str(obj1))
print(str(obj))   

