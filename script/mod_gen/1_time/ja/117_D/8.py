def f(X, A):
    N = len(A)
    return sum(X ^ A[i] for i in range(N))

if __name__ == '__main__':
    f()