def concat(seq, n):
    if n == 1:
        return seq
    else:
        return concat(seq, n-1) + [n] + seq

if __name__ == '__main__':
    concat()