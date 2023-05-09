def f(A, B):
    if A == B:
        return A
    elif A == 0:
        return f(1, B)
    elif A % 2 == 0:
        return f(A + 1, B) ^ A
    else:
        return f(A - 1, B) ^ A
A, B = map(int, input().split())
print(f(A, B))

if __name__ == '__main__':
    f()