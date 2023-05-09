def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * (N-1)
    for i in range(N):
        for j in range(i+1, N):
            d = min(j-i, abs(X-i)+abs(Y-j)+1)
            dist[d-1] += 1
    for d in dist:
        print(d)

if __name__ == '__main__':
    main()