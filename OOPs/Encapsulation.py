# modify the car class to encapsulate the brand attribute 
# making it privatr and provide the getter method for it 


 # to make varible private in python we __ before the var name 
class Car :
    def __init__ (self , brand , name):
        self.__brand = brand
        self.name = name
    def get_met(self) :
        return self.__brand + "  tkc"
    def full_name(self) :
        return f"{self.__brand}  {self.name}" 
my_car = Car("lambo" , "kali");
#print(my_car.__brand); # we cannot access because it is now private
print(my_car.get_met())