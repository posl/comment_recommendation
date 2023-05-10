def count_shout(A, B, K):
    if A >= B:
        return 0
    else:
        count = 1
        num = A * K
        while num < B:
            num = num * K
            count += 1
        return count
