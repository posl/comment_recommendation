def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(n):
            tmp.append(cakes[j][0] * ((i >> 0) & 1) + cakes[j][1] * ((i >> 1) & 1) + cakes[j][2] * ((i >> 2) & 1))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

if __name__ == '__main__':
    main()