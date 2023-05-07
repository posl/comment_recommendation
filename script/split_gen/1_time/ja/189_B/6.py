def solve():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P
        if X < 0 and ans == -1:
            ans = i + 1
    print(ans)
