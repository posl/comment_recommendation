def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min_val = N + 1
    ans = 0
    for i in range(N):
        if P[i] <= min_val:
            ans += 1
            min_val = P[i]
    print(ans)
