def f(x):
    res = 0
    for i in range(1, x+1):
        if x % i == 0:
            res += 1
    return res

if __name__ == '__main__':
    f()