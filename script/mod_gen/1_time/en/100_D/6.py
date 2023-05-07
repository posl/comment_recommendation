def main():
    n, m = [int(i) for i in input().split()]
    cakes = []
    for i in range(n):
        cakes.append([int(i) for i in input().split()])
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * n
        for j in range(3):
            if (i >> j) & 1:
                for k in range(n):
                    tmp[k] += cakes[k][j]
            else:
                for k in range(n):
                    tmp[k] -= cakes[k][j]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

if __name__ == '__main__':
    main()