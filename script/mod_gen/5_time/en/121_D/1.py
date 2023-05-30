def f(A, B):
    if A == B:
        return A
    elif A % 2 == 0 and B % 2 == 0:
        return f(A // 2, B // 2) * 2
    elif A % 2 == 0 and B % 2 != 0:
        return f(A // 2, B // 2) * 2 + 1
    elif A % 2 != 0 and B % 2 == 0:
        return f(A // 2, B // 2) * 2 + 1
    else:
        return f(A // 2, B // 2) * 2 + 2
A, B = map(int, input().split())
print(f(A, B))
