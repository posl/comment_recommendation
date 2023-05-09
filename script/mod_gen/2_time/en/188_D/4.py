def main():
    N, C = map(int, input().split())
    services = []
    for i in range(N):
        a, b, c = map(int, input().split())
        services.append((a, c))
        services.append((b + 1, -c))
    services.sort()
    ans = 0
    sum = 0
    last = 0
    for i in range(len(services)):
        if i == 0:
            last = services[i][0]
        if last != services[i][0]:
            ans += min(sum, C) * (services[i][0] - last)
            last = services[i][0]
        sum += services[i][1]
    print(ans)

if __name__ == '__main__':
    main()