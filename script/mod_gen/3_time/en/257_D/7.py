def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A = sorted(A, key=lambda x: x[2])
    INF = 10 ** 9 + 7
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][2] * 2 >= abs(A[i][0] - A[j][0]) + abs(A[i][1] - A[j][1]):
                dist[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, dist[i][j])
    print(ans - 1)

if __name__ == '__main__':
    main()