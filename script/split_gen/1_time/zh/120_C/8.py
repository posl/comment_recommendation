def solve():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == "1":
            ans += 1
    ans = min(ans, N-ans)
    print(ans)
solve()
