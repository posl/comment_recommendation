def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        sign = [-1, -1, -1]
        if i & 1:
            sign[0] = 1
        if i & 2:
            sign[1] = 1
        if i & 4:
            sign[2] = 1
        cakes.sort(key=lambda x: sum([sign[j] * x[j] for j in range(3)]), reverse=True)
        tmp = 0
        for j in range(M):
            tmp += sum([sign[k] * cakes[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()