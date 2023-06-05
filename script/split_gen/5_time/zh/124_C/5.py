def solve(S):
    N = len(S)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                ans += 1
        else:
            if S[i] == '1':
                ans += 1
    return min(ans, N - ans)
S = input()
print(solve(S))
