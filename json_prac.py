import json

job = {"title": "AI Engineer", "company": "Acme", "requirements": ["python", "sql"]}

with open("job.json", "w") as f:
    json.dump(job, f, indent=2)       # dict -> file

with open("job.json", "r") as f:
    loaded = json.load(f)             # file -> dict

print(loaded["title"])                # AI Engineer
print(loaded["requirements"][0])      # python