#count +ve numbers
ml = [];
count = 0;
for i in range(10) :
    ml.append(int(input()));
for i in ml :
    if i>0 :
        count+=1;
print();
print(count);


# sum of even numbers ;
l = [1,2,3,4,5,6,7,8,9];
sum = 0;
for i in l:
    if i%2==0 :
        sum+=i;
print(sum);

 # reverse string
l = 'nsjkdnbfjb';
print(l[::-1]);

# reverse a string using a loop 
s = "mdakfmlwkd";
ans = "";
for ch in range(len(s)-1 , -1 , -1) :
    ans+=s[ch];
print(ans);

# find first non repeated character in string

s = "aaaaaabbbbbc";
for char in s:
    if s.count(char)==1:
        print(char);
        break;


#factorial

n = 5;
mul = 1;
while(n!=0):
    mul = mul*n;
    n-=1;
print(mul);

