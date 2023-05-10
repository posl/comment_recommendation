def problems103_a():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])
