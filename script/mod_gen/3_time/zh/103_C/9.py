def f(m, a):
    sum = 0
    for i in a:
        sum += m % i
    return sum

if __name__ == '__main__':
    f()