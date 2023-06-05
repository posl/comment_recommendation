def getMissingNumber(S):
    a = [0] * 10
    for i in S:
        a[int(i)] = 1
    for i in range(10):
        if a[i] == 0:
            return i
