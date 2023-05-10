def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in reversed(range(N)):
        for j in reversed(range(i)):
            if (A[i] + A[j]) % 2 == 0:
                return A[i] + A[j]
    return -1
print(solve())
