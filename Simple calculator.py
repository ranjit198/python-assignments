#Simple Basic calculator
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
def add (x , y):
        return(x + y)
def subtract(x , y):
        return(x - y)
def multiply(x , y):
        return(x * Y)
def divide(x , y):
        if y!=0:
                return(x / y)
        else:
                print("the number is 0 so, it can't be divisible")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 1:
    result = add(num1, num2)
    print(f"The addition of these numbers is: {result}")
elif choice == 2:
    result = subtract(num1, num2)
    print(f"The subtraction of these numbers is: {result}")
elif choice == 3:
    result = multiply(num1, num2)
    print(f"The multiplication of these numbers is: {result}")
elif choice == 4:
    result = divide(num1, num2)
    if result == "Error: Division by zero is not allowed":
        print(result)
    else:
        print(f"The division of these numbers is: {result}")
else:
    print("Invalid choice")
