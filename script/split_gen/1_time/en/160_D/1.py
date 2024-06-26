def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist[min(j - i, abs(X - i) + abs(Y - j) + 1) - 1] += 1
    for i in range(N - 1):
        print(dist[i])
