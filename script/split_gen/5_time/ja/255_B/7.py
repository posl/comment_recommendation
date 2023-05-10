def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for i in range(n)]
    ans = 10**18
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            d = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if d > ans:
                continue
            cnt = 0
            for m in range(n):
                x, y = xy[m]
                for l in a:
                    if ((x1-x)**2 + (y1-y)**2)**0.5 < l or ((x2-x)**2 + (y2-y)**2)**0.5 < l:
                        cnt += 1
                        break
            if cnt == n:
                ans = min(ans, d)
    print(ans)
