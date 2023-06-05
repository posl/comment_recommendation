def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    for i in range(N):
        if i == 0:
            min_h = A[i]
        else:
            if A[i] - min_h > 1:
                return 1
            else:
                min_h = A[i]
    return 0
print(solve())
