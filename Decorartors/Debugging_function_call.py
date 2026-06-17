# create a decorator to print the function name and its arguments every time 
# the function is called
def helper(func) :
    def wrapper(*args , **kwargs) :
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k , v in kwargs.items())
        print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args , **kwargs)
    return wrapper

@ helper
def greet(name , greeting = "hello") :
    print(f"{greeting}{name}")
greet("love ")