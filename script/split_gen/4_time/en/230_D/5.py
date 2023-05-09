def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key=lambda x: x[0])
    ans = 0
    while walls:
        ans += 1
        L, R = walls.pop(0)
        while walls and walls[0][0] <= R + D:
            L, R = walls.pop(0)
        R += D
        while walls and walls[0][0] <= R + D:
            L, R = walls.pop(0)
    print(ans)
