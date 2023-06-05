def count_student(N,P,student_score):
    count = 0
    for i in range(N):
        if student_score[i] < P:
            count += 1
    return count

if __name__ == '__main__':
    count_student()