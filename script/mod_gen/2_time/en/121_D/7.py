def f(A, B):
    if A == 0:
        return B
    else:
        return f(A-1, B) ^ (A-1)

if __name__ == '__main__':
    f()