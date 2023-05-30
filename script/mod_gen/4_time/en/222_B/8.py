def failed_students():
    n, p = map(int, input().split())
    score = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if score[i] < p:
            count += 1
    print(count)
failed_students()
