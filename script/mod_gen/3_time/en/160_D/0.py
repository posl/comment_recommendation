def main():
    N, X, Y = map(int, input().split())
    dist = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + abs(Y - j) + 1)
            dist[d] += 1
    for i in range(1, N):
        print(dist[i])

if __name__ == '__main__':
    main()