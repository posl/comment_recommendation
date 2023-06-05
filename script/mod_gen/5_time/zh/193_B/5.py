def solve(N, A, P, X):
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1 or result > P[i]:
                result = P[i]
    return result

if __name__ == '__main__':
    solve()