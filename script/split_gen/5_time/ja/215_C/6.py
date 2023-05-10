def getPermutation(s, k):
    if len(s) == 1:
        return s
    n = len(s)
    fact = 1
    for i in range(2, n):
        fact *= i
    q, r = divmod(k, fact)
    return s[q] + getPermutation(s[:q] + s[q+1:], r)
s, k = input().split()
k = int(k)
s = sorted(s)
print(getPermutation(s, k-1))
