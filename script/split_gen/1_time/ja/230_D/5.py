def main():
    n, d = map(int, input().split())
    wall = []
    for _ in range(n):
        l, r = map(int, input().split())
        wall.append((r, l))
    wall.sort()
    ans = 0
    for i in range(n):
        if wall[i][1] > d:
            ans += 1
            d = wall[i][0]
        else:
            d = min(d, wall[i][0])
    ans += 1
    print(ans)
