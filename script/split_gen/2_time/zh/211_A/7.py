def problems210_d():
    h,w,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    min_a = [[0]*w for _ in range(h)]
    min_a[0][0] = a[0][0]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                min_a[i][j] = min_a[i][j-1] + c
            elif j == 0:
                min_a[i][j] = min_a[i-1][j] + c
            else:
                min_a[i][j] = min(min_a[i-1][j],min_a[i][j-1]) + c
            min_a[i][j] = min(min_a[i][j],a[i][j])
    min_b = [[0]*w for _ in range(h)]
    min_b[h-1][w-1] = a[h-1][w-1]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            elif i == h-1:
                min_b[i][j] = min_b[i][j+1] + c
            elif j == w-1:
                min_b[i][j] = min_b[i+1][j] + c
            else:
                min_b[i][j] = min(min_b[i+1][j],min_b[i][j+1]) + c
            min_b[i][j] = min(min_b[i][j],a[i][j])
    min_a_b = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            min_a_b[i][j] = min(min_a[i][j],min_b[i][j])
    ans = 10**18
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                ans = min(ans,min_a_b[i][j]+min_a_b[i][j-1]+c)
            elif j == 0
