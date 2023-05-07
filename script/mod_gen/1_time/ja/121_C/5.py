def main():
    N, M = map(int, input().split())
    shops = []
    for _ in range(N):
        A, B = map(int, input().split())
        shops.append((A, B))
    shops.sort()
    cost = 0
    for A, B in shops:
        if M <= B:
            cost += A * M
            break
        else:
            cost += A * B
            M -= B
    print(cost)

if __name__ == '__main__':
    main()