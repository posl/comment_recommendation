def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        n = len(s)
        a = 1
        for i in range(n):
            a *= (i + 1)
        b = a / n
        c = k / b
        d = k % b
        if d == 0:
            c -= 1
            d = b
        return s[c] + getPermutation(s[0:c] + s[c + 1:n], d)

if __name__ == '__main__':
    getPermutation()