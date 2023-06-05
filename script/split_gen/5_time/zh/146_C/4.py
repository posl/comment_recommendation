def f(A, B, X):
    if A + B > X:
        return 0
    elif A * 10 + B * 1 <= X:
        return 10
    else:
        for i in range(1, 10):
            if A * i + B * len(str(i)) > X:
                return i - 1
        return 0
