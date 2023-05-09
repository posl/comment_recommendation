def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    xy.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            a = xy[j][1] - xy[i][1]
            b = xy[j][0] - xy[i][0]
            p = xy[i][0] - a
            q = xy[i][1] + b
            r = xy[j][0] - a
            s = xy[j][1] + b
            if [p, q] in xy and [r, s] in xy:
                ans += 1
    print(ans//2)
