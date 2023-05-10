def solve():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                continue
            for k in range(j+1, N):
                if points[j][0] == points[k][0]:
                    continue
                if points[i][1] == points[k][1]:
                    continue
                for l in range(k+1, N):
                    if points[k][1] == points[l][1]:
                        continue
                    if points[l][0] == points[i][0] and points[l][1] == points[j][1]:
                        ans += 1
    print(ans)
