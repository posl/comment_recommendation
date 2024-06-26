def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    t = 0
    for i in range(N-1):
        t += A[i]
        if t > T:
            print('No')
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                if t > T:
                    print('No')
                    return
    print('Yes')
