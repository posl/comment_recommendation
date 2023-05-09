def count_bottoms(s):
    n = len(s)
    ans = 0
    for i in range(n-1):
        if s[i] == 'v' and s[i+1] == 'w':
            ans += 1
    return ans
