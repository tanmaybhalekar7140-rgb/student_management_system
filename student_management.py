import csv
import os

FILE_NAME = "students.csv"
FIELDS = ["id", "name", "age", "course"]


def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_students(students):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def find_student(students, student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def add_student():
    students = load_students()
    student_id = input("Enter ID: ").strip()
    if not student_id:
        print("ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("A student with this ID already exists.")
        return
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    if not age.isdigit():
        print("Age must be a number.")
        return
    course = input("Enter course: ").strip()
    students.append({"id": student_id, "name": name, "age": age, "course": course})
    save_students(students)
    print("Student added successfully.")


def update_student():
    students = load_students()
    student = find_student(students, input("Enter ID to update: ").strip())
    if not student:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    student["name"] = input(f"Name [{student['name']}]: ").strip() or student["name"]
    new_age = input(f"Age [{student['age']}]: ").strip()
    if new_age:
        if not new_age.isdigit():
            print("Age must be a number. Update cancelled.")
            return
        student["age"] = new_age
    student["course"] = input(f"Course [{student['course']}]: ").strip() or student["course"]
    save_students(students)
    print("Student updated successfully.")


def delete_student():
    students = load_students()
    student = find_student(students, input("Enter ID to delete: ").strip())
    if not student:
        print("Student not found.")
        return
    students.remove(student)
    save_students(students)
    print("Student deleted successfully.")


def search_student():
    students = load_students()
    student = find_student(students, input("Enter ID to search: ").strip())
    if student:
        print(f"\nID: {student['id']} | Name: {student['name']} | "
              f"Age: {student['age']} | Course: {student['course']}")
    else:
        print("Student not found.")


def display_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print(f"\n{'ID':<10}{'Name':<20}{'Age':<6}{'Course':<20}")
    print("-" * 56)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['age']:<6}{s['course']:<20}")


def main():
    actions = {
        "1": add_student,
        "2": update_student,
        "3": delete_student,
        "4": search_student,
        "5": display_students,
    }
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student by ID")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()