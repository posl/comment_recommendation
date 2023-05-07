def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist2 = 0
            for k in range(D):
                dist2 += (X[i][k] - X[j][k]) ** 2
            if dist2 ** 0.5 == int(dist2 ** 0.5):
                cnt += 1
    print(cnt)
