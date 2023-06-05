def sequence(n):
    if n == 1:
        return [1]
    else:
        seq = sequence(n-1)
        return seq + [n] + seq
