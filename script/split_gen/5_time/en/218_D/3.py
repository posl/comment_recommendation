def main():
    N = int(input())
    xy = [list(map(int, input().split())) for i in range(N)]
    xy.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            if x1 < x2 and y1 < y2:
                if [x1, y2] in xy and [x2, y1] in xy:
                    ans += 1
    print(ans)
