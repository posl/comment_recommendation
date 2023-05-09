def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (xy[j][1]-xy[i][1]) / (xy[j][0]-xy[i][0]) <= 1:
                ans += 1
    print(ans)
