# program to make simple calculator
# defining the functions

def add(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x,y):
    return x/y

def power(x,y):
    return pow(x,y)

#Taking inputs from the user
print("Select the operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Devide")
print("5.Power")
choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", substraction(num1,num2))
elif choice == '3':
    print(num1, "x", num2, "=", multiply(num1,num2))
elif choice == '4':
    print(num1, "/", num2, "=", devide(num1,num2))
elif choice == '5':
    print(num1, "^", num2, "=", power(num1,num2))
else:
    print("Invalid")
