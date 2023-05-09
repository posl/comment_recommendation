def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = [0] * N
        for j in range(N):
            if i & 1:
                tmp[j] += cake[j][0]
            else:
                tmp[j] -= cake[j][0]
            if i & 2:
                tmp[j] += cake[j][1]
            else:
                tmp[j] -= cake[j][1]
            if i & 4:
                tmp[j] += cake[j][2]
            else:
                tmp[j] -= cake[j][2]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

if __name__ == '__main__':
    main()