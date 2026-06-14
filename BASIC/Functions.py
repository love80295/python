# create a function to calculate square of a number
def sq(number):
   return number ** 2;

print(sq(4));

# create a function for addition of two number

def sum(num1 , num2) :
   return num1+num2;

res = sum(2 , 3); # function with two parameters
print(res);

# # default with parameter
def greet(name = 'love'):
   return 'hello ' + name;
print(greet('y'));

# lamda function (function without name);
# write a lamda function to calculate the cube of a number

cube  = lambda x : x**3;
print(cube(3));

s1 = lambda x1 , x2 : x1+x2;
print(s1(2,3));

# write a function to add all the parameters till n

def res(*args) :
    return sum(args);
print(res(1,2,3,4,5));

# # kwarags

def fun(**kwargs):
    for key , value in kwargs.items():
        print(f"the {key} is {value}");

print(fun(name = 'love' , power = 'CEO'));

# concept of yeild  (it oresave itself)

def even(limit):
    for i in range(2 , limit+1 , 2):
        yield i;
for num in even(10):
    print(num)

# create a recursive function to calculate factorial

def fact(num):
    if(num == 0) :
        return 1
    return num * fact(num-1);

print(fact(5));

