def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i):
            for k in range(j):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    pass
                else:
                    ans += 1
    print(ans)
