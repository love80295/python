# write a decorator that measure the time taken by the function to execute
import time; 
def timer(func) :
    def wrapper(*args) :
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@ timer 
def example_function(n) :
    time.sleep(n)

example_function(2);

# decorators are used to modify the fucntion 
# matlab main function ko execute karane se phele use kisi aur function ke through  guzarna 
# isis ko hi decorators khehe te h 