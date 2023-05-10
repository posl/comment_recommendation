def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(N):
        for j in range(i + 1, N):
            dist[min(j - i, abs(X - i) + 1 + abs(Y - j))] += 1
    for i in range(1, N):
        print(dist[i])
