# add a static method to a class that add a general descruption 
# of a car

# static methods are those which are accessible to class only 
# not objects example 

class Car :
    total = 0;
    def __init__ (self , brand , name):
        self.brand = brand
        self.name = name
        Car.total+=1;
    def full_name(self) :
        return f"{self.brand}  {self.name}"   
    def fuel_type(self) :
        return "petrol or deisel" 
    @staticmethod
    def general() :
        return "bdkbcsdjbvhdjbvdjhkfbvhd";
class Ec(Car) :
    def __init__ (self , brand , name , size):
        super().__init__(brand , name)
        self.size = size
    def fuel_type(self) :
        return "electric charge"    
    
petrol = Car("tata" , "safari");
# print(petrol.fuel_type());
tesla = Ec("tesla" , "model S" , 23554353);
# print(tesla.fuel_type());
# print(Car.total);
print(tesla.general());  # should avoid
print(Car.general());