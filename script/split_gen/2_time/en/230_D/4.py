def main():
    n, d = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(n)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < n:
        ans += 1
        j = i + 1
        while j < n and walls[j][0] < walls[i][1]:
            j += 1
        i = j
    print(ans)
