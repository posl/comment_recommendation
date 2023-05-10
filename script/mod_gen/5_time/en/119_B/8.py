def otoshidama(n, x, u):
    sum = 0
    for i in range(n):
        if u[i] == "JPY":
            sum += x[i]
        else:
            sum += x[i] * 380000.0
    return sum

if __name__ == '__main__':
    otoshidama()