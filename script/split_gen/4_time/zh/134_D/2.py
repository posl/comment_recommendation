def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
    for i in range(1, n + 1):
        if a[i - 1] == 1:
            for j in range(i * 2 - 1, n, i):
                b[j] = 1
    if sum(b) == 0:
        print(0)
    else:
        print(sum(b))
        for i in range(n):
            if b[i] == 1:
                print(i + 1, end=' ')
        print()
