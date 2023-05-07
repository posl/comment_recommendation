def takoyaki(N, X, T):
    if N <= X:
        return T
    else:
        return (N // X) * T + takoyaki(N % X, X, T)
