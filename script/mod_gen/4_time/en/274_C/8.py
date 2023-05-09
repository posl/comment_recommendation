def amoebas(n, a):
    result = [0] * (2 ** (n + 1))
    for i in range(n):
        result[a[i]] = 1
    for i in range(1, n + 1):
        for j in range(2 ** (i - 1), 2 ** i):
            result[j * 2] = result[j]
            result[j * 2 + 1] = result[j]
    return result

if __name__ == '__main__':
    amoebas()