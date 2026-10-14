skills=[]

with open("my_Skills.txt","r")as f:
    for line in f:
        skills.append(line.strip().lower())

print("Loaded" , len(skills), "skills")
for skill in skills:
    print(skill)

new_skill = input("add a skill: ")

with open("my_Skills.txt","a")as f:
    f.write(new_skill.strip().lower() + "\n")

print("Saved")
