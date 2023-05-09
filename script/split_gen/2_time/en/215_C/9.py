def solve(s,k):
    if len(s) == 1:
        return s
    s = list(s)
    s.sort()
    n = len(s)
    for i in range(n):
        if s[i] != s[0]:
            break
    if i == 1:
        return s[0] + solve(s[1:],k)
    if k <= i * factorial(n-1):
        return s[0] + solve(s[1:],k)
    else:
        return s[i] + solve(s[:i] + s[i+1:],k-i*factorial(n-1))
s,k = input().split()
k = int(k)
print(solve(s,k))
