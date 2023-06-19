def getSecret(N, X, A):
    A = [A[i] - 1 for i in range(N)]
    friends = [False] * N
    friends[X - 1] = True
    for i in range(N):
        if friends[A[i]]:
            friends[i] = True
    return sum(friends)

if __name__ == '__main__':
    getSecret()