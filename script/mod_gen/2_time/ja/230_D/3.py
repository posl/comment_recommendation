def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if walls[i][1] - walls[i][0] + 1 < D:
            continue
        ans += 1
        j = i + 1
        while j < N and walls[j][0] <= walls[i][0] + D - 1:
            j += 1
        i = j - 1
    print(ans)

if __name__ == '__main__':
    main()