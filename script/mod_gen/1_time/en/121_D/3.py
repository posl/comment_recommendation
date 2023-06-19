def f(A, B):
    if A == B:
        return A
    elif A % 2 == 0 and B % 2 == 0:
        return 0 ^ f(A + 1, B - 1)
    elif A % 2 == 0 and B % 2 == 1:
        return 1 ^ f(A + 1, B - 1)
    elif A % 2 == 1 and B % 2 == 0:
        return A ^ f(A + 1, B - 1)
    elif A % 2 == 1 and B % 2 == 1:
        return (A + 1) ^ f(A + 1, B - 1)
A, B = map(int, input().split())
print(f(A, B))
