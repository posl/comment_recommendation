def pascal_triangle(n):
    pascal_triangle = []
    for i in range(n):
        pascal_triangle.append([1]*(i+1))
        if i > 1:
            for j in range(1,i):
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
    return pascal_triangle
n = int(input())
pascal_triangle = pascal_triangle(n)
for i in range(n):
    print(*pascal_triangle[i])

if __name__ == '__main__':
    pascal_triangle()