def f(m):
    sum = 0
    for i in range(N):
        sum += m % a[i]
    return sum

if __name__ == '__main__':
    f()