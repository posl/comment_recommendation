def seq(n):
    if n == 1:
        return [1]
    else:
        s = seq(n-1)
        return s + [n] + s

if __name__ == '__main__':
    seq()