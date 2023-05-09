def main():
    N, M = map(int, input().split())
    K = [0] * M
    X = [0] * M
    for i in range(M):
        K[i], *X[i] = map(int, input().split())
    for i in range(M):
        for j in range(i + 1, M):
            if len(set(X[i]) & set(X[j])) == 0:
                print('No')
                return
    print('Yes')
