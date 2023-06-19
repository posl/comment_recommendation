def f(a, b):
    if a == b:
        return a
    else:
        return a ^ f(a + 1, b)
A, B = map(int, input().split())
print(f(A, B))
