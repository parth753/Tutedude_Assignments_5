
students_marks = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 92,
    'Diana': 88,
    'Ethan': 76
}

students = input("Enter the student's name: ")

if(students in students_marks):
    print(f"{students}'s marks: {students_marks[students]}")
else:
    print("Student not found")