def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 10 ** 20
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(n):
                if l + 1 in a:
                    continue
                if x[i] == x[j]:
                    t = abs(x[i] - x[l])
                elif y[i] == y[j]:
                    t = abs(y[i] - y[l])
                else:
                    t = ((x[i] - x[l]) ** 2 + (y[i] - y[l]) ** 2) ** 0.5
                ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    main()