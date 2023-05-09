def solve():
    N = int(input())
    A = list(map(int, input().split()))
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    s.sort()
    ans = 0
    for i in range(N):
        ans = max(ans, s[i + 1] - s[i])
    print(ans)
