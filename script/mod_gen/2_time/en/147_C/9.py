def f(i, x, y, n, a, xij, yij):
    if i == n:
        return 0
    if y[i] == 1:
        if x[i] == 1:
            if a[i] == 0:
                return 1 + f(i + 1, x, y, n, a, xij, yij)
            else:
                for j in range(a[i]):
                    if xij[i][j] != 1:
                        return 0
                return 1 + f(i + 1, x, y, n, a, xij, yij)
        else:
            if a[i] == 0:
                return f(i + 1, x, y, n, a, xij, yij)
            else:
                for j in range(a[i]):
                    if xij[i][j] == 1:
                        return 0
                return f(i + 1, x, y, n, a, xij, yij)
    else:
        if x[i] == 1:
            if a[i] == 0:
                return f(i + 1, x, y, n, a, xij, yij)
            else:
                for j in range(a[i]):
                    if xij[i][j] == 1:
                        return 0
                return f(i + 1, x, y, n, a, xij, yij)
        else:
            if a[i] == 0:
                return 1 + f(i + 1, x, y, n, a, xij, yij)
            else:
                for j in range(a[i]):
                    if xij[i][j] != 1:
                        return 0
                return 1 + f(i + 1, x, y, n, a, xij, yij)

if __name__ == '__main__':
    f()