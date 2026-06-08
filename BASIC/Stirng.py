a = "lovre agrawal";
# string in python '' , "" , """  """ ,
print(a)
slice = a[0:8]; # slicing in two parameters
print(slice)
slice2 = a[0:8:2]; # 2 ke gap me print hogaye means 1 number skip hogayega 2 par , 3 par 2 
print(slice2);
print(a.upper()); # converts in uppercase
bc = '        ajdfdsndoindionav';
print(bc.strip()) ; # bydefault space 
print(bc.replace("aj" , "tmkb"));
b = "l , 0 , n , j ,";
print(b.split(", ")); # split the string on the basis of argument
print(b.find('sdjnk')) # gives the index of the string or the character you passed
# if not found print -1;
print(b.count("0")); # count the number of times string ouccer
c = ['a' , 'b' , 'c' , 'd' , 'e'];
print(" ".join(c)); # it converts the list of string  into single string
print(len(b)); # gives len of the string
print("a" in bc); # it states does this string is in given varible or not\

