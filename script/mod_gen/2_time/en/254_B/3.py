def pascal_triangle(n):
    if n == 0:
        return [1]
    else:
        return [1] + [pascal_triangle(n-1)[i] + pascal_triangle(n-1)[i+1] for i in range(n-1)] + [1]
N = int(input())
for i in range(N):
    print(*pascal_triangle(i))

if __name__ == '__main__':
    pascal_triangle()