def calc(a, b, k):
    if a >= k:
        a -= k
        return a, b
    else:
        b -= (k - a)
        a = 0
        if b >= 0:
            return a, b
        else:
            b = 0
            return a, b

if __name__ == '__main__':
    calc()