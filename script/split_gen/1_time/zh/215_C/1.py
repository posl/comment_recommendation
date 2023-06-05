def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        for i in range(len(s)):
            if k <= factorial(len(s) - 1):
                return s[i] + getPermutation(s[:i] + s[i+1:], k)
            else:
                k -= factorial(len(s) - 1)
        return s[0] + getPermutation(s[1:], k)
