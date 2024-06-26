def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d]) ** 2
            dist = int(dist ** 0.5)
            if dist ** 2 == dist:
                ans += 1
    print(ans)
