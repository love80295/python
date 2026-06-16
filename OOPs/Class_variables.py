# add a class variable to car that will keep track of 
# numbers of car created 
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
class Ec(Car) :
    def __init__ (self , brand , name , size):
        super().__init__(brand , name)
        self.size = size
    def fuel_type(self) :
        return "electric charge"    
    
petrol = Car("tata" , "safari");
print(petrol.fuel_type());
tesla = Ec("tesla" , "model S" , 23554353);
print(tesla.fuel_type());
print(Car.total);