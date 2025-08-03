# functions and interaction with user

def greet_karan_code(name):
    print(f"Hello,{name}!")
def learning_Skills_add(skills,skill):
    skills.append(skill)
    return skills
def show_skills(skills):
    i = 0
    for s in skills:
        i=i+1
        print(f"\nSkill {i}. {s}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet_karan_code(name)
    skills = []

    print("Please enter skills, once adding all Skills, Then type done :")
    while True:
        skill = input("Add Skill or type done: ")
        if skill.lower() == "done" :
            break
        skills = learning_Skills_add(skills,skill) 
    show_skills(skills)
