number = int(input("Input total elements to be in the list = "))
list1 = []
count = 0
while(count < number):
    num = int(input("Enter the number : "))
    list1.append(num)
    count = count + 1
print(list1)
for current in list1:
        if(current > 0):
            print(current)
