ml = [1,2,3,4,5,6,7,8];
for i in range(len(ml)):
    print(i);
ml.append(98); # add element in list
print(ml[len(ml)-1]);
print(ml.pop());
print(ml.remove(ml[2])); # it will print none kyuki remove kuch return nahi karta 
print(ml)
ml.insert(2 ,  3); # insert at any place you want
print(ml);
# interesting interview question
ml2 = ml ; 
ml2 = ml.copy();
# what is the difference between these two 
# main differnce is in 1st one same reference is passed in ml2 but in 2nd one new copy of ml is generated in the memory and its reference is also different


 # LIST COMPREHENSION

abcd = [x**2 for x in range(10)];
print(abcd);

# all other methods are same in list as of string