def buy_product(N, X, A):
    for i in range(N):
        if i % 2 == 0:
            X -= A[i]
        else:
            X -= A[i] - 1
    if X >= 0:
        return "Yes"
    else:
        return "No"
