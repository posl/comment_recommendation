def f(a,b,k):
    if a == 0:
        return "b"*b
    elif b == 0:
        return "a"*a
    elif k <= 1:
        return "a"*a + "b"*b
    else:
        if k <= comb(a+b-1, a-1):
            return "a" + f(a-1, b, k-1)
        else:
            return "b" + f(a, b-1, k-comb(a+b-1, a-1))
