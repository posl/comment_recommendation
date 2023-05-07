def main():
    N = int(input())
    A = list(map(int, input().split()))
    dist = [0] * (2 * N + 1)
    for i in range(N):
        dist[A[i]] = 0
        dist[2 * A[i]] = dist[A[i]] + 1
        dist[2 * A[i] + 1] = dist[A[i]] + 1
    print(*dist[1:], sep='
')

if __name__ == '__main__':
    main()