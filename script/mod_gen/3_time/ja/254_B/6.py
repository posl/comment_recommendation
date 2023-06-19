def pascal_triangle(n):
    if n == 0:
        return [1]
    else:
        pt = pascal_triangle(n-1)
        pt = [0] + pt + [0]
        return [pt[i] + pt[i+1] for i in range(len(pt)-1)]
n = int(input())
for i in range(n):
    print(*pascal_triangle(i))
