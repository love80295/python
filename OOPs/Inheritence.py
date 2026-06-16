# create a electric car class that inherit the properties of 
# Car , and EC also has the additional properties called Battery_Size
class Car :
    def __init__ (self , brand , name):
        self.brand = brand
        self.name = name
    def full_name(self) :
        return f"{self.brand}  {self.name}"    
class Ec(Car) :
    def __init__ (self , brand , name , size):
        super().__init__(brand , name)
        self.size = size
my_car = Car("lambo" , "urus");
my_Ec_car = Ec("lambo" , "urus" , 2300)
print(my_Ec_car.full_name());