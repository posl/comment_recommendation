def permutation(a,b,k):
    if a == 0 or b == 0:
        return "a"*a + "b"*b
    elif k <= 0:
        return "a"*a + "b"*b
    else:
        count = 1
        for i in range(1,a+b+1):
            count *= i
        for i in range(1,a+1):
            count /= i
        for i in range(1,b+1):
            count /= i
        if k <= count:
            return "a" + permutation(a-1,b,k)
        else:
            return "b" + permutation(a,b-1,k-count)
