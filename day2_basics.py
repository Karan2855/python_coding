# --- Day 2: Python Control Flow & Data Types ---

# 🔹 Data Types
my_string = "Python is powerful!"
my_int = 30
my_float = 99.9
my_bool = True
my_list = ["Python", "SQL", "Cloud", "AI"]
my_dict = {"name": "Karan", "target": "30LPA+"}

print("--- Data Types ---")
print(type(my_string), type(my_list), type(my_dict))

# 🔹 If-Else
print("\n--- If-Else ---")
salary = 20
if salary >= 30:
    print("Goal achieved 🎉")
else:
    print("Keep pushing 🚀")

# 🔹 Loops
print("\n--- Loops ---")
for tech in my_list:
    print(f"Learning: {tech}")

# 🔹 While Loop
print("\n--- While Loop ---")
count = 1
while count <= 3:
    print(f"Round {count}")
    count += 1

# 🔹 Challenge: Categorize a number
print("\n--- Challenge ---")
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")