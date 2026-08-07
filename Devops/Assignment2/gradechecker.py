# 1. Grade Checker

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# 2. Student Grades

students = {}

name = input("Enter student name: ")
grade = input("Enter grade: ")

students[name] = grade

update = input("Do you want to update a grade? (yes/no): ")

if update == "yes" or update == "y":
    name = input("Enter student name to update: ")

    if name in students:
        new_grade = input("Enter new grade: ")
        students[name] = new_grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

print("\nStudent Grades:")

for name, grade in students.items():
    print(name, ":", grade)

# 3. Write to a File

file = open("sample.txt", "w")

file.write("This is my Python Project 1.\n")
file.write("I am learning file handling in Python.")

file.close()

print("\nData written to file successfully.")

# 4. Read from a File

file = open("sample.txt", "r")

content = file.read()

print("\nFile Content:")
print(content)

file.close()