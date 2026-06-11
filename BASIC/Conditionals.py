# 1 --> age group
# x = int(input());
# if x<13:
#     print("child");
# elif x>=13 and x<18 :
#     print("teenage");
# elif x>=18 and x<62 :
#     print("adult");
# else:
#     print("old age");

# 2 --> movie pricing

x = int(input());
day = input();
if x<18 :
    if day=="wednesday" :
        print("$6");
    else:
        print("$8");
else :
    if day=="wednesday" :
        print("$10");
    else :
        print("$12");

