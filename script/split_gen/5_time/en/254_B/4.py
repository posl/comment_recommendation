def pascal_triangle(n):
    result = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)
    return result
n = int(input())
result = pascal_triangle(n)
for row in result:
    print(' '.join(map(str, row)))
