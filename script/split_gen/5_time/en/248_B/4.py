def answer(A, B, K):
    count = 0
    while A < B:
        A *= K
        count += 1
    return count
