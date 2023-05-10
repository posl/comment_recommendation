def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    #print(a)
    #print(a[0][0])
    #print(a[n-1][n-1])
    max = 0
    for i in range(n):
        for j in range(n):
            #print(i, j)
            #print(a[i][j])
            #print(a[n-1-i][n-1-j])
            if i == 0 and j == 0:
                continue
            elif i == n-1 and j == n-1:
                continue
            else:
                #print(a[i][j] + a[n-1-i][n-1-j])
                if max < (a[i][j] + a[n-1-i][n-1-j]):
                    max = a[i][j] + a[n-1-i][n-1-j]
    if n % 2 == 0:
        print(max)
    else:
        print(max + a[int(n/2)][int(n/2)])
