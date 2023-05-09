def main():
    N, D = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    wall.sort(key=lambda x:x[0])
    ans = 0
    while len(wall) > 0:
        ans += 1
        wall.sort(key=lambda x:x[0])
        now = wall[0][0]
        del wall[0]
        for i in range(len(wall)):
            if wall[i][0] <= now < wall[i][1]:
                wall[i][0] = now + D
            if wall[i][1] <= now + D:
                del wall[i]
                break
    print(ans)
