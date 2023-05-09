def f(A, B):
    if A == B:
        return A
    if A % 2 == 0:
        if B % 2 == 0:
            return f(A + 1, B - 1) ^ A ^ B
        else:
            return f(A + 1, B) ^ A
    else:
        if B % 2 == 0:
            return f(A, B - 1) ^ B
        else:
            return f(A + 1, B - 1)
A, B = map(int, input().split())
print(f(A, B))

if __name__ == '__main__':
    f()