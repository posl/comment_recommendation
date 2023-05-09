def calc(n, d):
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    return sum

if __name__ == '__main__':
    calc()