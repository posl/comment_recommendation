def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        sign = [-1, -1, -1]
        if (i & 1):
            sign[0] = 1
        if (i & 2):
            sign[1] = 1
        if (i & 4):
            sign[2] = 1
        cakes.sort(key=lambda x: sum([sign[j] * x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([abs(sum([sign[j] * cakes[k][j] for j in range(3)])) for k in range(M)]))
    print(ans)

if __name__ == '__main__':
    main()