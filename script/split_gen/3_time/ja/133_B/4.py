def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k])**2
            if int(d**0.5)**2 == d:
                cnt += 1
    print(cnt)
