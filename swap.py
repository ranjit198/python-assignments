a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap the values without using a third variable
a = a + b
b = a - b
a = a - b
# Print the swapped values
print(f"After swapping, the first number is: {a}")
print(f"After swapping, the second number is: {b}")
