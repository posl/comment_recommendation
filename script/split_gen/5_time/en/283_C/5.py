def solve():
    S = input()
    S = S[::-1]
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        elif i == 1:
            ans += int(S[i]) * 2
        else:
            ans += int(S[i]) * (10 ** (i - 1)) * (i - 1) + 10 ** (i - 1)
    print(ans)
