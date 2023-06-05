def pascal_triangle(n):
    L = [1]
    yield L
    for i in range(n-1):
        L = [1] + [L[j] + L[j+1] for j in range(len(L) - 1)] + [1]
        yield L
n = int(input())
for i in pascal_triangle(n):
    print(' '.join(map(str,i)))
