def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        ans = 2 * sum(A[N//2:]) - 2 * sum(A[:N//2]) - A[N//2] + A[N//2-1]
    else:
        ans = 2 * sum(A[N//2+1:]) - 2 * sum(A[:N//2]) + max(A[N//2] - A[N//2-1], A[N//2+1] - A[N//2])
    print(ans)
