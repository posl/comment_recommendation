def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    tmp[j] += cake[j][k]
                else:
                    tmp[j] -= cake[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

if __name__ == '__main__':
    main()