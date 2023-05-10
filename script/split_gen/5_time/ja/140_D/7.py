def solve(n,k,s):
    ans = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 1
    ans += min(2*k, ans+2)
    return ans
