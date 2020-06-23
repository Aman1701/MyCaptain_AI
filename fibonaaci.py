num = input("Enter total fibonacci elements to be printed : ")
n = int(num)
print(n)
count = 0
a=0
b=1
print(a)
print(b)
while(count < n-2):
    c = a+b
    print(c)
    a=b
    b=c
    count = count + 1
