def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if walls[i][0] - 1 > ans:
            ans += (walls[i][0] - 1 - ans) // D + 1
        ans += (walls[i][1] - walls[i][0] + 1) // D
    print(ans)

if __name__ == '__main__':
    main()