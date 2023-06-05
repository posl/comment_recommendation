def f(x):
    result = 0
    for i in range(1, x+1):
        if x % i == 0:
            result += 1
    return result

if __name__ == '__main__':
    f()