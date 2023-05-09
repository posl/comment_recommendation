def solve(s):
    ans = 0
    atcoder = "atcoder"
    for i in range(len(s)):
        if s[i] == atcoder[i]:
            continue
        else:
            ans += 1
    return ans
