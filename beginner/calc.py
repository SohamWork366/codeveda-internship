def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Error: Division by zero(0) not possible!!"
    return a/b

first_number = float(input("Enter first number:"))
second_number = float(input("Enter second number:"))

a = first_number
b = second_number

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

task = int(input("Enter operation to be performed(1,2,3,4):"))

if task == 1:
    print(addition(a,b))
elif task == 2:
    print(subtraction(a,b))
elif task == 3:
    print(multiplication(a,b))
elif task == 4:
    print(division(a,b))
else:
    print("Invalid Task!!!")