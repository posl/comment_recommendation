def count_failed_student(N, P, scores):
    count = 0
    for i in range(N):
        if scores[i] < P:
            count = count + 1
    return count

if __name__ == '__main__':
    count_failed_student()