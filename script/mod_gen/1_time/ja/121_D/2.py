def f(a, b):
    if a == 0:
        return b
    else:
        return f(a-1, b) ^ f(a-1, a-1)
A, B = map(int, input().split())
print(f(A, B))
