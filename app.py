# print ("Hello World")

print("Welcome to my State-of-the-art Calculator")
op = ['Addition', 'Subtraction', 'Multiplication', "Division"]

i = 1
for x in op:
    print(str(i) + ". " +x)
    i +=1

a1 = input("Please enter the first value:")
a2 = input("Please enter the second value:")

a = input("Please choose the operation:")
if a=='1':
    print("The sum of these two numbers: " + str(int(a1)+int(a2)))




