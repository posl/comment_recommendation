def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            d = 0
            for k in range(D):
                d += (X[i][k] - X[j][k]) ** 2
            if d ** 0.5 == int(d ** 0.5):
                count += 1
    print(count)
