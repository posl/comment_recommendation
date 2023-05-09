def f(A, B):
    if A == 0:
        return B
    else:
        return f(0, B) ^ f(0, A-1)

if __name__ == '__main__':
    f()