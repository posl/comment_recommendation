def problems254_b():
    n = int(input())
    a = []
    b = []
    for i in range(1, n+1):
        a.append([])
        for j in range(1, i+1):
            if j == 1 or j == i:
                a[i-1].append(1)
            else:
                a[i-1].append(b[i-2][j-2] + b[i-2][j-1])
        b.append(a[i-1])
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=' ')
        print()
