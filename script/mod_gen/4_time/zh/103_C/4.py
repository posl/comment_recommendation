def f(m, a):
    result = 0
    for i in a:
        result += m % i
    return result

if __name__ == '__main__':
    f()