def main():
    N, D = map(int,input().split())
    wall = []
    for i in range(N):
        L, R = map(int,input().split())
        wall.append([L,R])
    wall.sort()
    ans = 0
    for i in range(N):
        if wall[i][0] < wall[i-1][1]:
            wall[i][1] = min(wall[i-1][1], wall[i][1])
        if wall[i][1] - wall[i][0] + 1 >= D:
            ans += 1
            wall[i][0] = wall[i][1] - D + 1
    print(ans)
