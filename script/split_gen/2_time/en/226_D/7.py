def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.sort()
    X = [xy[0] for xy in XY]
    Y = [xy[1] for xy in XY]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(X[i]-X[j])+abs(Y[i]-Y[j]))
    print(ans)
