def pascal_triangle(n):
    if n == 1:
        return [1]
    else:
        p = pascal_triangle(n-1)
        return [1] + [p[i]+p[i+1] for i in range(n-2)] + [1]
N = int(input())
for i in range(N):
    print(*pascal_triangle(i+1))
