# implement the decorator that return  cache values if the function is called
# with same arguments then besides reexecuting the function return the 
# cached values
import time
def helper(func) :
    cache_values = {}
    print(cache_values)
    def wrapper(*args) :
        if args in cache_values :
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper


@ helper
def long_running_function(a,b) :
    time.sleep(4)
    return a+b
print(long_running_function(2,3));
print(long_running_function(2,3));
print(long_running_function(4,3));



