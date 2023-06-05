def solve(n,m,s,t):
    for i in range(n):
        for j in range(m):
            if s[i]==t[j]:
                return -1
    for i in range(n):
        for j in range(n):
            if i!=j:
                for k in range(m):
                    if s[i]+t[k]==s[j]:
                        return -1
                    if t[k]+s[i]==s[j]:
                        return -1
    ans = ""
    for i in range(n):
        ans += s[i]
        if i!=n-1:
            ans += "_"
    return ans
