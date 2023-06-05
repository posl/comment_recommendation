def getKthCommonDivisor(A, B, K):
    if A > B:
        A, B = B, A
    count = 0
    for i in range(1, B + 1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                return i
    return 0
