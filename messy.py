students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88]
]

NAME_INDEX = 0
SCORE_START_INDEX = 1
NUMBER_OF_SCORES = 3

def sum_scores(student_record):
    """Return the total of numeric scores in a student record, skipping the name."""
    total = 0
    for index in range(SCORE_START_INDEX, len(student_record)):
        total = total + student_record[index]
    return total

def average_score(student_record):
    return sum_scores(student_record) / NUMBER_OF_SCORES

def count_students_above_class_average(student_records):
    """Return how many students have an average strictly above the class average."""
    class_average_total = 0
    for student in student_records:
        class_average_total = class_average_total + average_score(student)
    class_average = class_average_total / len(student_records)
    count = 0
    for student in student_records:
        if average_score(student) > class_average:
            count = count + 1
    return count

print("REPORT")

for student in students:
    total = sum_scores(student)
    average = average_score(student)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{student[NAME_INDEX]}{total}{average}{grade}")

class_average_total = 0

for student in students:
    average = average_score(student)
    class_average_total = class_average_total + average

print(f"Class average:{class_average_total / len(students)}")
print(f"Students above class average:{count_students_above_class_average(students)}")

highest_average = 0
topper_name = ""

for student in students:
    average = average_score(student)

    if average > highest_average:
        highest_average = average
        topper_name = student[NAME_INDEX]

print(f"Topper:{topper_name}{highest_average}")
