def pascal_triangle(n): # n is number of rows
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
n = int(input())
for row in pascal_triangle(n):
    print(*row)

if __name__ == '__main__':
    pascal_triangle()