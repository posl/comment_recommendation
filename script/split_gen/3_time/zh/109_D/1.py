def func(h, w, a):
    n = 0
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j]%2 == 1 and j != w-1:
                a[i][j] -= 1
                a[i][j+1] += 1
                n += 1
                ans.append([i+1, j+1, i+1, j+2])
            elif a[i][j]%2 == 1 and i != h-1:
                a[i][j] -= 1
                a[i+1][j] += 1
                n += 1
                ans.append([i+1, j+1, i+2, j+1])
    print(n)
    for i in range(n):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])
