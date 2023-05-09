def solve():
    S = input()
    t = 'atcoder'
    ans = 0
    for i in range(len(S)):
        if S[i] != t[i]:
            ans += 1
    print(ans)
