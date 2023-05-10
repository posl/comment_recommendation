def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            distance = 0
            for k in range(D):
                distance += (X[i][k] - X[j][k]) ** 2
            if int(distance ** 0.5) ** 2 == distance:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()