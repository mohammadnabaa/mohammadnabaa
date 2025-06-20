def get_students_data(n, students=None):
    """Recursively collect student names and grades."""
    if students is None:
        students = []

    if n == 0:
        return students

    name = input(f"Enter name of student #{len(students) + 1}: ")
    while True:
        try:
            grade = float(input(f"Enter grade for {name} (out of 100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    students.append((name, grade))
    return get_students_data(n - 1, students)

def display_student_summary(students):
    print("\n--- Student Grades ---")
    for name, grade in students:
        print(f"{name}: {grade}")

def get_avg_grade(students):
    total = sum(grade for _, grade in students)
    return total / len(students) if students else 0

def get_highest_grade(students):
    highest = max(students, key=lambda x: x[1])
    return highest

def count_passed(students):
    passed = [s for s in students if s[1] >= 60]
    return len(passed)

def main():
    try:
        num = int(input("Enter the number of students: "))
        if num <= 0:
            print("Number must be positive.")
            return
    except ValueError:
        print("Invalid number.")
        return

    students = get_students_data(num)
    
    display_student_summary(students)
    avg = get_avg_grade(students)
    highest_name, highest_grade = get_highest_grade(students)
    passed_count = count_passed(students)

    print("\n--- Summary ---")
    print(f"Class Average: {avg:.2f}")
    print(f"Highest Grade: {highest_name} with {highest_grade}")
    print(f"Number of Students Passed: {passed_count}")

if _name_ == "_main_":
    main()