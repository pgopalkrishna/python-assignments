student_grades= [{"name": "Alice", "grade": 85},
                 {"name": "Bob", "grade": 92},
                 {"name": "Charlie", "grade": 78}]

# adding a new student to the list
new_student = {"name": "David", "grade": 88}
student_grades.append(new_student)

#updating a student's grade
student_grades[0]["grade"] = 90 

#printing the grades of all students
for student in student_grades:
    name = student["name"]
    grade = student["grade"]
    if grade >= 90:
        print(f"{name}'s grade is A")
    elif grade >= 80 and grade <= 89:
        print(f"{name}'s grade is B")
    elif grade >= 70 and grade <= 79:
        print(f"{name}'s grade is C")
    elif grade >= 60 and grade <= 69:
        print(f"{name}'s grade is D")
    else:
        print(f"{name}'s grade is F")

