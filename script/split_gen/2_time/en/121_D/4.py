def f(A, B):
    if A == B:
        return A
    else:
        return f(A//2, B//2) * 2 + (B % 2) - (A % 2)
A, B = map(int, input().split())
print(f(A, B))
