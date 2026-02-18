from skills_db import SKILLS
from career_map import ROLE_SKILLS

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().lower()

# read files
resume = read_file("resume.txt")
job = read_file("job.txt")

matched = []
missing = []

for skill in SKILLS:
    if skill in job:
        if skill in resume:
            matched.append(skill)
        else:
            missing.append(skill)

total = len(matched) + len(missing)

if total > 0:
    match_percent = (len(matched) / total) * 100
else:
    match_percent = 0

print("\n✅ MATCHED SKILLS:")
for s in matched:
    print("-", s)

print("\n❌ MISSING SKILLS:")
if missing:
    for s in missing:
        print("-", s)
else:
    print("None 🎉 Your resume matches all tracked skills.")

print(f"\n🎯 MATCH SCORE: {match_percent:.2f}%")

print("\n💡 IMPROVED SUMMARY FOR YOUR RESUME:")
print("Python Developer skilled in", ", ".join(matched[:5]), "with interest in machine learning and backend development.")
print("\n🎯 CAREER SUGGESTIONS:")

eligible_roles = []
target_roles = []

for role, skills in ROLE_SKILLS.items():
    missing_for_role = [s for s in skills if s not in resume]

    if len(missing_for_role) == 0:
        eligible_roles.append(role)
    else:
        target_roles.append((role, missing_for_role))

# roles you already match
if eligible_roles:
    print("\n✅ You are currently suitable for:")
    for role in eligible_roles:
        print("-", role)

# roles you can target by learning skills
print("\n🚀 You can target these roles if you learn:")
for role, skills in target_roles:
    print(f"\n→ {role}")
    for s in skills:
        print("  -", s)

print("\n🛠 RESUME IMPROVEMENT GUIDE:")

if missing:
    print("\nTo improve your chances for this job:")

    for skill in missing:
        print(f"\n👉 Add skill: {skill}")

        if skill in ["v"]:
            print("Where to add: Technical Skills section")
            print(f"Example line: Experienced in {skill} for backend development.")

        elif skill in ["pandas", "numpy", "matplotlib", "data science"]:
            print("Where to add: Projects or Skills section")
            print(f"Example line: Used {skill} for data analysis and processing.")

        elif skill in ["machine learning", "deep learning"]:
            print("Where to add: Projects section")
            print("Example line: Built predictive models using machine learning techniques.")

        elif skill in ["html", "css", "javascript", "node js"]:
            print("Where to add: Technical Skills section")
            print(f"Example line: Developed web interfaces using {skill}.")

        else:
            print("Where to add: Skills section")
            print(f"Example line: Knowledge of {skill}.")
else:
    print("Your resume already matches the key skills for this job 🎉")