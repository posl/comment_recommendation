def pascal_triangle(n):
    a = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i+1):
            if (j == 0 or j == i):
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a
n = int(input())
a = pascal_triangle(n)
for i in range(n):
    for j in range(i+1):
        if j == i:
            print(a[i][j])
        else:
            print(a[i][j], end=" ")
