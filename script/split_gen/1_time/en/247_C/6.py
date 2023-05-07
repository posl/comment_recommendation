def getSequence(n):
    if n == 1:
        return [1]
    else:
        seq = getSequence(n-1)
        return seq + [n] + seq
