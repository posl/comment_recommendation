def printAll(n, m, prefix):
    if n == 0:
        print(prefix)
    else:
        for i in range(1, m + 1):
            printAll(n - 1, m, prefix + ' ' + str(i))
