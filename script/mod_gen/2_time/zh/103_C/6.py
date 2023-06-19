def f(m, a):
    result = 0
    for i in range(len(a)):
        result += m % a[i]
    return result

if __name__ == '__main__':
    f()