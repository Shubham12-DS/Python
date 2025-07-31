# 🔥 CGPA Calculator – Grade Input Version
# - Input: Grades (O, A1, B2, etc.)
# - No marks needed
# - Flexible semesters (ask at end)
# - Full report with SGPA & CGPA
# By Shubham

# Grade to Grade Point Mapping
GRADE_TO_GP = {
    'O': 10,
    'A1': 9,
    'A2': 8,
    'B1': 7,
    'B2': 6,
    'C1': 5,
    'C2': 4,
    'D': 3,
    'E': 0
}

# Optional: Grade descriptions
GRADE_MEANING = {
    'O': 'Outstanding',
    'A1': 'Excellent',
    'A2': 'Very Good',
    'B1': 'Good',
    'B2': 'Above Average',
    'C1': 'Average',
    'C2': 'Below Average',
    'D': 'Pass',
    'E': 'Fail'
}

# 🚀 Start of Program
print("=" * 85)
print("📊 CGPA CALCULATOR – GRADE INPUT MODE")
print("📌 Enter grades directly (e.g., O, A1, B2). No marks needed!")
print("=" * 85)

# Step 1: Enter subjects (minimum 4)
subjects = []
print("\n📋 Enter subject names (minimum 4). Type 'done' to stop after 4.\n")

while len(subjects) < 4:
    sub = input(f"Subject {len(subjects) + 1}: ").strip()
    if sub.lower() == 'done' and len(subjects) >= 4:
        break
    if sub == "" or sub.lower() == 'done':
        print("⚠️  At least 4 subjects required.")
        continue
    subjects.append(sub)

# Add more subjects
while True:
    more = input("\n➕ Add another subject? (yes/no): ").strip().lower()
    if more in ['yes', 'y']:
        new_sub = input("Subject name: ").strip()
        if new_sub:
            subjects.append(new_sub)
        else:
            print("❌ Invalid name.")
    else:
        break

print(f"\n✅ Total Subjects: {len(subjects)} → {', '.join(subjects)}")

# Step 2: Enter grades for each semester
all_semesters = []  # Each semester: list of (grade, gp)
sem_count = 1

print("\n📥 Now enter grades semester by semester.")
print("You can enter as many semesters as completed. CGPA will be calculated later.\n")

while True:
    print(f"\n🎯 ENTER GRADES FOR SEMESTER {sem_count}")
    sem_data = []

    for sub in subjects:
        while True:
            grade = input(f"  ➡️  {sub}: ").strip().upper()
            if grade in GRADE_TO_GP:
                gp = GRADE_TO_GP[grade]
                sem_data.append((grade, gp))
                break
            else:
                print(f"    ❌ Invalid grade. Valid grades: {list(GRADE_TO_GP.keys())}")
    
    all_semesters.append(sem_data)
    sem_count += 1

    # Ask if more semesters
    more = input("\n📌 Enter next semester? (yes/no): ").strip().lower()
    if more not in ['yes', 'y']:
        break

# Step 3: Ask how many semesters to include in CGPA (at the end!)
print("\n" + "-" * 60)
print("🎯 FINAL STEP: How many semesters to include in CGPA?")
for i in range(1, len(all_semesters) + 1):
    print(f"{i} → Include Semester 1 to {i}")
print("-" * 60)

while True:
    try:
        n = int(input(f"Enter number (1 to {len(all_semesters)}): "))
        if 1 <= n <= len(all_semesters):
            break
        else:
            print(f"❌ Please enter between 1 and {len(all_semesters)}.")
    except ValueError:
        print("❌ Enter a valid number.")

# Step 4: Calculate SGPA for each of the first `n` semesters
sgpas = []
for i in range(n):
    total_gp = sum(data[1] for data in all_semesters[i])
    sgpa = total_gp / len(subjects)
    sgpas.append(sgpa)

# Final CGPA
cgpa = sum(sgpas) / len(sgpas)
percentage = cgpa * 9.5  # CBSE-style approximation

# Step 5: Display Full Report
print("\n" + "=" * 100)
print("🎓 FINAL ACADEMIC REPORT".center(100))
print("=" * 100)

# Header
print(f"{'Subject':<15}", end="")
for i in range(1, n + 1):
    print(f"Sem{i} Grade  ", end="")
print()

print("-" * 100)

# Subject rows
for idx, sub in enumerate(subjects):
    print(f"{sub:<15}", end="")
    for sem_idx in range(n):
        grade, gp = all_semesters[sem_idx][idx]
        print(f"{grade:<11}", end="")
    print()

print("-" * 100)

# SGPA Row
print(f"{'SGPA':<15}", end="")
for i in range(n):
    print(f"{sgpas[i]:<11.2f}", end="")
print()

print("-" * 100)
print(f"🎯 CGPA (based on {n} semester(s)): {cgpa:.2f}")
print(f"📌 Approximate Percentage (CBSE-style): {percentage:.2f}%")
print("=" * 100)

# Optional: Show grade key
show_key = input("\nShow grade key? (yes/no): ").strip().lower()
if show_key in ['yes', 'y']:
    print("\n📘 Grade Key:")
    for g, desc in GRADE_MEANING.items():
        print(f"{g} → {desc}")
