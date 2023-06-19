def f(n):
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i
    return res

if __name__ == '__main__':
    f()