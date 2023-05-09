def f(A, B):
    if (A == B):
        return A
    else:
        return A ^ f(A + 1, B)

if __name__ == '__main__':
    f()