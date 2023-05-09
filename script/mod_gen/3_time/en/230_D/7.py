def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        end = walls[i][0] + D - 1
        while i < N and walls[i][0] <= end:
            end = min(end, walls[i][1] + D - 1)
            i += 1
    print(ans)
main()

if __name__ == '__main__':
    main()