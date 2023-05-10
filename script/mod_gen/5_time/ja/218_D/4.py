def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                    ans += 1
    print(ans//2)

if __name__ == '__main__':
    solve()