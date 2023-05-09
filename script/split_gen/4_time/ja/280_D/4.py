def solve(K):
    if K % 2 == 0 or K % 5 == 0:
        return -1
    else:
        i = 1
        while True:
            if (10**i - 1) % K == 0:
                return i
            else:
                i += 1
