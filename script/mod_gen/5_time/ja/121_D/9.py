def f(A, B):
    if A == B:
        return A
    if A == 0:
        if B % 4 == 0:
            return B
        if B % 4 == 1:
            return 1
        if B % 4 == 2:
            return B + 1
        if B % 4 == 3:
            return 0
    return f(0, A - 1) ^ f(0, B)
A, B = map(int, input().split())
print(f(A, B))
