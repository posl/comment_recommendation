def main():
    N, D = map(int, input().split())
    walls = [tuple(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i
        while j < N and walls[j][0] + D - 1 >= walls[i][1]:
            j += 1
        i = j
    print(ans)

if __name__ == '__main__':
    main()