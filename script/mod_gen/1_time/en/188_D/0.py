def main():
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append([a, c])
        AB.append([b+1, -c])
    AB.sort(key=lambda x: x[0])
    ans = 0
    cost = 0
    t = 0
    for ab in AB:
        ans += min(C, cost)*(ab[0]-t)
        cost += ab[1]
        t = ab[0]
    print(ans)

if __name__ == '__main__':
    main()