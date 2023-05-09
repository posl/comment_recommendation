def f(num):
    if num == 0:
        return 1
    else:
        return num * f(num - 1)

if __name__ == '__main__':
    f()