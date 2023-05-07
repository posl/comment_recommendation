def f(n):
    return n / sum(int(i) for i in str(n))

if __name__ == '__main__':
    f()