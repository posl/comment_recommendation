def sequence(n):
    if n == 1:
        return [1]
    else:
        s = sequence(n-1)
        return s + [n] + s

if __name__ == '__main__':
    sequence()