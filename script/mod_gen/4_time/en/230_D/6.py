def main():
    N, D = map(int, input().split())
    walls = []
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key = lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        l = walls[i][0]
        r = walls[i][1]
        while i < N - 1 and walls[i + 1][0] <= r + 1:
            r = max(r, walls[i + 1][1])
            i += 1
        ans += (r - l) // D + 1
        i += 1
    print(ans)

if __name__ == '__main__':
    main()