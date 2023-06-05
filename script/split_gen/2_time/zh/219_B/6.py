def exam_grade(n):
    if n < 40:
        return 40 - n
    elif n < 70:
        return 70 - n
    elif n < 90:
        return 90 - n
    else:
        return 'expert'
n = int(input())
print(exam_grade(n))
