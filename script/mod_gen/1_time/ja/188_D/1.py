def main():
    N, C = map(int, input().split())
    service = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        service.append((a, c))
        service.append((b+1, -c))
    service.sort()
    ans = 0
    cost = 0
    prev = 0
    for i in range(2*N):
        ans += min(cost, C) * (service[i][0] - prev)
        cost += service[i][1]
        prev = service[i][0]
    print(ans)
main()

if __name__ == '__main__':
    main()