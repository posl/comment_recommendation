def f(n):
    r = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            r += i
            if n // i != i:
                r += n // i
    return r

if __name__ == '__main__':
    f()