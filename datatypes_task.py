# Integer variable
age = 22
# Float variable
height = 5.8
# String variable
name = "Varun"
# Boolean variable
is_student = True
# Printing variables and their types
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Name:", name, "| Type:", type(name))
print("Is Student:", is_student, "| Type:", type(is_student))

print("\n--- Arithmetic Operations ---")
# Arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\n--- Type Conversion ---")
# Taking user input
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
try:
    # Converting string input to integer
    num1_int = int(num1)
    num2_float = float(num2)
    result = num1_int + num2_float
    print("Sum after conversion:", result)
except ValueError:
    print("Invalid input! Please enter numeric values only.")
print("\n--- String Concatenation ---")
# Correct concatenation
print("My name is " + name + " and my age is " + str(age))
print("\n--- Dynamic Typing Demo ---")
x = 1
print("x =", x, "Type:", type(x))
x = "Now I am a string"
print("x =", x, "Type:", type(x))
