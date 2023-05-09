def main():
    N, X, Y = map(int, input().split())
    dist = [0] * (N - 1)
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            dist[min(j - i, abs(i - X) + 1 + abs(j - Y))] += 1
    for i in range(1, N):
        print(dist[i])
