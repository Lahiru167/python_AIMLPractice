from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
class car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

obj = car()
obj.start_engine()
obj.stop_engine()