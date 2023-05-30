def f():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                return -1
        if len(set(A)) == 1:
            return count
print(f())
