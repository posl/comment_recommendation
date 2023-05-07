def f(A, B):
    def f1(N):
        if N % 2 == 0:
            return N
        else:
            return 1 - N
    return f1(A - 1) ^ f1(B)

if __name__ == '__main__':
    f()