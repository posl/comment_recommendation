def main():
    N, D = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    wall.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if wall[i][1] - wall[i][0] + 1 >= D:
            ans += 1
        else:
            for j in range(i + 1, N):
                if wall[j][0] <= wall[i][1] + D:
                    wall[j][0] = wall[i][1] + 1
                else:
                    break
    print(ans)
