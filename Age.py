age = int(input("Enter your age: "))
if age < 18:
    category = "minor"
elif 18 <= 65:
    category = "adult"
else:
    category = "senior"
print(f"You are an {category}.")