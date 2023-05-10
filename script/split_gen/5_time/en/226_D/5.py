def solve():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = towns[i]
            x2, y2 = towns[j]
            dx = x2 - x1
            dy = y2 - y1
            cnt = 0
            for k in range(N):
                x3, y3 = towns[k]
                if (x3+dx, y3+dy) in towns:
                    cnt += 1
            ans = max(ans, cnt)
    print(N-ans)
