def bounce(N, X, L):
    D = 0
    count = 0
    for i in range(N):
        D = D + L[i]
        if D <= X:
            count = count + 1
    return count + 1

if __name__ == '__main__':
    bounce()