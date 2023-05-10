def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                return A[i] + A[j]
    return -1
