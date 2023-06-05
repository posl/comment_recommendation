def func(N):
    k = 0
    while True:
        if 2**k > N:
            k -= 1
            break
        k += 1
    return k
