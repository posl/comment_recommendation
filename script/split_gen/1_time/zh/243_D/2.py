def solve(n,x,s):
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans//2
        elif s[i] == 'L':
            ans = ans*2
        elif s[i] == 'R':
            ans = ans*2 + 1
    return ans
