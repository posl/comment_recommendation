def solve(s):
    ans = 0
    t = 'atcoder'
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            ans += 1
    return ans
