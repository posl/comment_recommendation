def f(m, a):
    sum = 0
    for i in range(len(a)):
        sum += m % a[i]
    return sum

if __name__ == '__main__':
    f()