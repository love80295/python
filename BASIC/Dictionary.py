dict = {
    1 : '23',
    2 : '24',
    3: '56',
}
print(dict[2]); # get the value of the key
dict[2] = 7378;
print(dict[2]); # update the key
for key in dict:  # i will get the keys 
    print(key);
for key in dict:   # i will get the values
    print(dict[key]);
if 2 in dict:
    print("tmkc");
else:
    print("sbnjfv");
dict[4] = '235'; ## add new key and value
print(dict);
print(dict.pop(2)); # pop the key and its value which you gave 

# there are dictionary in dictionary {{}}
dict1 = {
    1 : {
        12 : 23,
        13 : 24,
    },
    2 : {
        21 : 56,
        22 : 65,
    }
}
print(dict1[1][12])