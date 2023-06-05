def count_failed_students(students, pass_score):
    count = 0
    for student in students:
        if student < pass_score:
            count += 1
    return count
