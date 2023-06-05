def amidakuji(h,w,k):
    a = [0 for i in range(w-1)]
    for i in range(w-1):
        a[i] = [0 for j in range(h+1)]
    for i in range(w-1):
        a[i][0] = 1
    for i in range(1,h+1):
        for j in range(w-1):
            if j == 0:
                a[j][i] = a[j][i-1] + a[j+1][i-1]
            elif j == w-2:
                a[j][i] = a[j-1][i-1] + a[j][i-1]
            else:
                a[j][i] = a[j-1][i-1] + a[j][i-1] + a[j+1][i-1]
    return a[k-1][h] % 1000000007
