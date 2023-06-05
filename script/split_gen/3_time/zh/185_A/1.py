def problem185_a():
    A = input().split()
    for i in range(4):
        A[i] = int(A[i])
    A.sort()
    if A[0] + A[1] + A[2] >= A[3]:
        print(3)
    else:
        print(4)
