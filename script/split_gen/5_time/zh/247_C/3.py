def s(n):
    if n == 1:
        return [1]
    else:
        a = s(n - 1)
        return a + [n] + a
