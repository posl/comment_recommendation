def pascal_triangle(n):
    rows = []
    for i in range(n):
        rows.append([1]*(i+1))
        for j in range(1,i):
            rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
    return rows
n = int(input())
rows = pascal_triangle(n)
for row in rows:
    print(" ".join(map(str,row)))
