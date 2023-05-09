def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        xyz.sort(key=lambda x: (-(x[0] * ((i >> 2) % 2 * 2 - 1) + x[1] * ((i >> 1) % 2 * 2 - 1) + x[2] * (i % 2 * 2 - 1))))
        tmp = 0
        for j in range(M):
            tmp += xyz[j][0] * ((i >> 2) % 2 * 2 - 1) + xyz[j][1] * ((i >> 1) % 2 * 2 - 1) + xyz[j][2] * (i % 2 * 2 - 1)
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()