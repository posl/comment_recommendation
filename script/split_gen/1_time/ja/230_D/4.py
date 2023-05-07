def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])
    ans = 0
    r = 0
    for l, r in walls:
        if r < r:
            ans += 1
        else:
            r = l + D - 1
    print(ans)
