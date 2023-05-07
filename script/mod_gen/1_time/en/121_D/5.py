def f(A, B):
    if A == B:
        return A
    elif A + 1 == B:
        return A ^ B
    else:
        if A % 2 == 0:
            if B % 2 == 0:
                return f(A, B - 1) ^ B
            else:
                return f(A, B - 1)
        else:
            if B % 2 == 0:
                return f(A + 1, B) ^ A
            else:
                return f(A + 1, B - 1)
A, B = map(int, input().split())
print(f(A, B))

if __name__ == '__main__':
    f()