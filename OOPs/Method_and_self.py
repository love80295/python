class Car :
    def __init__ (self , brand , name):
        self.brand = brand
        self.name = name
    def full_name(self) :
        return f"{self.brand}  {self.name}"
my_car = Car("lambo" , "urus");
print(my_car.full_name());
