def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cakes[j][k] * ((i >> k) % 2 * 2 - 1) for k in range(3)]))
        tmp.sort()
        ans = max(ans, sum(tmp[-M:]))
    print(ans)

if __name__ == '__main__':
    main()