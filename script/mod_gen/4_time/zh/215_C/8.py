def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        n = len(s)
        f = [1]
        for i in range(1, n):
            f.append(f[i-1] * i)
        if k > f[n-1] * n:
            return "Error"
        else:
            for i in range(n):
                if k <= f[n-1]:
                    return s[0] + getPermutation(s[1:], k)
                else:
                    k -= f[n-1]
                    s = s[1:]

if __name__ == '__main__':
    getPermutation()