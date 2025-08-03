# day1_basics.py

# --- Day 1: Python Foundations ---

# Variables
name = "Karan"
goal = "₹30LPA+"
tech_stack = ["Python", "SQL", "Cloud", "AI/ML"]

# Functions
def intro(name, goal, stack):
    print(f"👋 Hi, I'm {name}!")
    print(f"My goal is {goal}")
    print("I'm learning:")
    for tech in stack:
        print(f"  - {tech}")

# Call function
intro(name, goal, tech_stack)