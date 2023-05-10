def max_value():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * (-1) ** (i // 4 % 2), x[1] * (-1) ** (i // 2 % 2), x[2] * (-1) ** (i % 2)))
        ans = max(ans, sum(sum(i) for i in zip(*cakes[:m])))
    print(ans)
max_value()

if __name__ == '__main__':
    max_value()