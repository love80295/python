# make model of a car read only 

# add a static method to a class that add a general descruption 
# of a car

# static methods are those which are accessible to class only 
# not objects example 

class Car :
    total = 0;
    def __init__ (self , brand , name):
        self.brand = brand
        self.__name = name
        Car.total+=1;
    def full_name(self) :
        return f"{self.brand}  {self.__name}"   
    def fuel_type(self) :
        return "petrol or deisel" 
    @staticmethod
    def general() :
        return "bdkbcsdjbvhdjbvdjhkfbvhd";
    @ property
    def name(self) :
        return self.__name
class Ec(Car) :
    def __init__ (self , __brand , name , size):
        super().__init__(__brand , name)
        self.size = size
    def fuel_type(self) :
        return "electric charge"    
    
petrol = Car("tata" , "safari");
# print(petrol.fuel_type());
tesla = Ec("tesla" , "model S" , 23554353);
# print(tesla.fuel_type());
# print(Car.total);
# print(tesla.general());
# tesla.name = "njen";
# print(tesla.name);  # !  it is changed 
#tesla.name = "dsnvjksd" # gives an eror you cannot change
print(tesla.name); # now you need to give the refernce of that method to access name 
