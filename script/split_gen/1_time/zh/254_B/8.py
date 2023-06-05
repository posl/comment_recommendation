def problems254_b():
    n = int(input())
    a = []
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a.append(1)
            else:
                a.append(a[-i]+a[-i-1])
        print(' '.join([str(a[i]) for i in range(len(a))]))
        a = []
