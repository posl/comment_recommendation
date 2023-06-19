def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

if __name__ == '__main__':
    s()