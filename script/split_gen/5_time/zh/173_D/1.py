def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    tmp = 0
    for i in range(N):
        tmp += A[i]
    ans = tmp
    for i in range(N):
        tmp += A[i+N] - A[i]
        ans = max(ans, tmp)
    print(ans)
