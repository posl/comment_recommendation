def f(x):
    ret = 0
    for i in range(1, x+1):
        if x % i == 0:
            ret += 1
    return ret

if __name__ == '__main__':
    f()