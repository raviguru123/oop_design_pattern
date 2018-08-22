from abc import ABCMeta, abstractmethod

class Obserever(metaclass = ABCMeta):
    @abstractmethod
    def Update(self, temprature, pressure, humidity):
        pass

class Display(metaclass = ABCMeta):

    @abstractmethod
    def Display(self):
        pass

class CurrentConditionsDisplay(Obserever, Display):

    def __init__(self):
        self.temprature = None
        self.humidity = None
        self.pressure = None

    def Display(self):
        print("<========CurrentConditionsDisplay==========>")
        print("temprature :", self.temprature)
        print("humidity :", self.humidity)
        print("pressure :", self.pressure)
        print("<========CurrentConditionsDisplay==========>")


    def Update(self, temprature, humidity, pressure):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.Display()
            

class StatisticsDisplay(Obserever, Display):
    
    def __init__(self):
        self.temprature = None
        self.humidity = None
        self.pressure = None

    def Display(self):
        print("<========StatisticsDisplay==========>")
        print("temprature :", self.temprature)
        print("humidity :", self.humidity)
        print("pressure :", self.pressure)
        print("<========StatisticsDisplay==========>")


    def Update(self, temprature, humidity, pressure):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.Display()

class ThirdPartyDisplay(Obserever,  Display):

    def __init__(self):
        self.temprature = None
        self.humidity = None
        self.pressure = None

    def Display(self):
        print("<========ThirdPartyDisplay==========>")
        print("temprature :", self.temprature)
        print("humidity :", self.humidity)
        print("pressure :", self.pressure)
        print("<========ThirdPartyDisplay==========>")


    def Update(self, temprature, humidity, pressure):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.Display()

class ForecastDisplay(Obserever, Display):
    def __init__(self):
        self.temprature = None
        self.humidity = None
        self.pressure = None

    def Display(self):
        print("<========ForecastDisplay==========>")
        print("temprature :", self.temprature)
        print("humidity :", self.humidity)
        print("pressure :", self.pressure)
        print("<========ForecastDisplay==========>")


    def Update(self, temprature, humidity, pressure):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.Display()



class Subject(metaclass = ABCMeta):
    @abstractmethod
    def RegisterObserver(self, obserever):
        pass
    
    @abstractmethod
    def RemoveObserver(self, obserever):
        pass
    
    @abstractmethod
    def NotifyObserver(self, obserever):
        pass




class WeatherData(Subject):
    observers = []
    temprature = None
    humidity = None
    pressure = None
    def RegisterObserver(self, observer):
        self.observers.append(observer())

    
    def RemoveObserver(self, observer):
        for o, index in enumerate(self.observers):
            if(o == observer):
                self.observers.pop(index)

    def NotifyObserver(self):
        for i  in self.observers:
            i.Update(self.temprature, self.humidity, self.pressure)
    
    def MeasurmentChanged(self):
        self.NotifyObserver()
    
    def setMeasurements(self, temprature, humidity, pressure):
        self.temprature = temprature
        self.humidity = humidity
        self.pressure = pressure
        self.MeasurmentChanged()


weather_obj = WeatherData()
weather_obj.RegisterObserver(ForecastDisplay)

weather_obj.setMeasurements(80, 65, 30.4);


weather_obj.RegisterObserver(ThirdPartyDisplay)
print("***************************************************")
weather_obj.setMeasurements(82, 70, 29.2);
weather_obj.RegisterObserver(CurrentConditionsDisplay)
print("***************************************************")
weather_obj.setMeasurements(78, 90, 29.2);
    




















