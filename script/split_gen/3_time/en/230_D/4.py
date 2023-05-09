def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort()
    ans = 0
    for i in range(N):
        if walls[i][0] <= D:
            ans += 1
            D = min(D, walls[i][1])
        else:
            break
    print(ans)
