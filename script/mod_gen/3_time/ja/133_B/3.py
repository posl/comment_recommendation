def solve():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k])**2
            if int(dist**0.5)**2 == dist:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()