def main():
    N, D = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    wall.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i
        while j < N and wall[j][0] <= wall[i][1] + D:
            j += 1
        i = j
        while i < N and wall[i][0] <= wall[j - 1][1] + D:
            i += 1
    print(ans)

if __name__ == '__main__':
    main()