def solve():
    N = int(input())
    x = [0] * 5
    for i in range(N):
        t, x[i], a = map(int, input().split())
        x[i] -= 1
    x.sort()
    ans = 0
    for i in range(1, N):
        if x[i] - x[i-1] > 1:
            ans += x[i] - x[i-1] - 1
    print(ans)
