def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            dist[d] += 1
    for k in range(1, N):
        print(dist[k])
