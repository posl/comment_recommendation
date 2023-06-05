def to_int(s, d):
    ans = 0
    for i in range(len(s)):
        ans = ans*10 + d[s[i]]
    return ans
