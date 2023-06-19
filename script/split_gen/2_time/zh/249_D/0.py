def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0
    for i in range(N):
        for j in range(N):
            if A[j] == 0:
                continue
            if A[i] % A[j] != 0:
                continue
            k = A[i] // A[j]
            if A.count(k) == 0:
                continue
            count += 1
    print(count)
