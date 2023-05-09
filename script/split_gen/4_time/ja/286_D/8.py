def pay(N, X, A, B):
    for i in range(N):
        X -= A[i] * B[i]
    if X >= 0:
        print('Yes')
    else:
        print('No')
