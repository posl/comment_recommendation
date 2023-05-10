def main():
    # input
    N, X = map(int, input().split())
    # A[i], B[i]
    AB = [list(map(int, input().split())) for _ in range(N)]
    # solve
    # 1. sort by A[i] + B[i]
    # 2. select minimum X stages
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for ab in AB[:X]:
        ans += ab[0] + ab[1]
    # 3. add remain stages
    for ab in AB[X:]:
        ans += ab[0]
    # output
    print(ans)

if __name__ == '__main__':
    main()