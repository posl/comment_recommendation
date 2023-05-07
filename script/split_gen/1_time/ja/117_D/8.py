def f(X, A):
    N = len(A)
    return sum(X ^ A[i] for i in range(N))
