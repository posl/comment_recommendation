def f(n, k):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            sum = sum + i * 100 + j
    return sum

if __name__ == '__main__':
    f()