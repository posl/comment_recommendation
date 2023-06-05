def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)
