def solve(N, Q, A, X):
    sum = 0
    for i in range(N-1):
        sum += abs(A[i] - A[i+1])
    for i in range(Q):
        if i == 0:
            print(sum + abs(A[0] - X[i]) + abs(X[i] - A[1]) - abs(A[0] - A[1]))
        elif i == Q-1:
            print(sum + abs(A[N-1] - X[i]) + abs(X[i] - A[N-2]) - abs(A[N-1] - A[N-2]))
        else:
            print(sum + abs(A[i] - X[i]) + abs(X[i] - A[i+1]) - abs(A[i] - A[i+1]) + abs(A[i+1] - X[i]) + abs(X[i] - A[i-1]) - abs(A[i+1] - A[i-1]))
        A[i] = X[i]
    return 0

if __name__ == '__main__':
    solve()