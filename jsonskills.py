import json

skills=[]

try:  
    with open("skills.json","r")as f:
        skills=json.load(f)
except FileNotFoundError :
    print("No skills file yet, starting fresh")
   
print("Loaded" , len(skills), "skills")
for skill in skills:
    print(skill)

new_skill = input("add a skill: ")
skills.append(new_skill.strip().lower())

with open("skills.json","w")as f:
    json.dump(skills, f, indent=2)       

print("Saved")
