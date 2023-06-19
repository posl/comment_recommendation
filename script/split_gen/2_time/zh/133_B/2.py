def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = sum(map(lambda x: (x[0]-x[1])**2, zip(X[i], X[j])))**0.5
            if dist.is_integer():
                cnt += 1
    print(cnt)
