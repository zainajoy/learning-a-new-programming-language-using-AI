# ================================
# PYTHON BEGINNER MASTER PROGRAM
# ================================

print("Welcome to Python Learning Program 🎉")
print("------------------------------------")

# --------------------------------
# 1. VARIABLES + INPUT + DATA TYPES
# --------------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("\nHello", name)
print("Next year you will be", age + 1)

# --------------------------------
# 2. MATH OPERATIONS
# --------------------------------
print("\n--- Math Section ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# --------------------------------
# 3. STRINGS
# --------------------------------
print("\n--- String Section ---")
sentence = input("Write a short sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Length:", len(sentence))

# --------------------------------
# 4. IF / ELSE CONDITIONS
# --------------------------------
print("\n--- Age Check ---")
if age >= 18:
    print("You are an adult ✅")
else:
    print("You are a minor ❌")

# --------------------------------
# 5. LOOPS (FOR LOOP)
# --------------------------------
print("\n--- Counting ---")
for i in range(1, 6):
    print("Number:", i)

# --------------------------------
# 6. LISTS
# --------------------------------
print("\n--- Favorite Foods ---")
foods = []

for i in range(3):
    food = input("Enter a favorite food: ")
    foods.append(food)

print("Your foods are:", foods)

# --------------------------------
# 7. FUNCTIONS
# --------------------------------
print("\n--- Functions ---")

def greet_user(user):
    print("Nice to meet you,", user)

greet_user(name)

def add_numbers(a, b):
    return a + b

result = add_numbers(num1, num2)
print("Function result:", result)

# --------------------------------
# 8. DICTIONARIES (Mini Database)
# --------------------------------
print("\n--- Simple Registration System ---")

user = {
    "username": input("Create username: "),
    "password": input("Create password: "),
    "email": input("Enter email: ")
}

print("\nRegistration Successful 🎉")
print("User details saved:")
print(user)

# --------------------------------
# 9. FINAL MESSAGE
# --------------------------------
print("\nCongratulations", name)
print("You just ran a Python program that uses MOST beginner concepts!")
