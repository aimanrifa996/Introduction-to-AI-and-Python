def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "Artificial Intelligence"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(subjects)
grade = calculate_grade(average)

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)

for i in range(len(subjects)):
    print(subjects[i] + ":", marks[i])

print("Total Marks:", total, "/", len(subjects) * 100)
print("Average:", round(average, 2), "%")
print("Grade:", grade)

if grade == "F":
    print("Result: Needs Improvement")
else:
    print("Result: PASS")
