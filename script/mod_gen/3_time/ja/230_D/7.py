def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    while walls:
        ans += 1
        start = walls[0][0]
        for i in range(len(walls)):
            if walls[i][0] - start >= D:
                walls = walls[i:]
                break
            if walls[i][1] - start >= D:
                walls = walls[i+1:]
                break
    print(ans)

if __name__ == '__main__':
    main()