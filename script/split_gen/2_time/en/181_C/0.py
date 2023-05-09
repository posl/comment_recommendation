def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (X[i] - X[j]) * (Y[i] - Y[k]) == (X[i] - X[k]) * (Y[i] - Y[j]):
                    print('Yes')
                    return
    print('No')
