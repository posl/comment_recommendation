def main():
    N = int(input())
    xy = []
    for _ in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))
    fact = [1]
    for i in range(1, N + 1):
        fact.append(fact[-1] * i)
    sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum += ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5
    print(sum * 2 / fact[N])

if __name__ == '__main__':
    main()