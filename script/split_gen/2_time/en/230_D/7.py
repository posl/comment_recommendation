def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        walls.append(list(map(int, input().split())))
    walls.sort(key=lambda x: x[0])
    # print(walls)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
            continue
        if walls[i][0] - walls[i-1][0] < D:
            if walls[i][1] - walls[i-1][1] < D:
                ans += 1
            else:
                ans += 1
        else:
            ans += 1
    print(ans)
