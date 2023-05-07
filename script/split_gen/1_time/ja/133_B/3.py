def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dis = 0
            for k in range(D):
                dis += (X[i][k] - X[j][k]) ** 2
            if dis ** 0.5 == int(dis ** 0.5):
                ans += 1
    print(ans)
