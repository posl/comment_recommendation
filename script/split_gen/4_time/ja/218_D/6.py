def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                for k in range(j+1, N):
                    if points[i][0] == points[k][0]:
                        ans += 1
            else:
                for k in range(j+1, N):
                    if points[i][0] != points[k][0] and points[j][0] != points[k][0]:
                        ans += 1
    print(ans)
