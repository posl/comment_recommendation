def f(A, B):
    if A == B:
        return A
    else:
        return A ^ B
A, B = map(int, input().split())
print(f(A, B))
