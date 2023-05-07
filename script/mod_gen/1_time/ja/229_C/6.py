def main():
    N, W = map(int, input().split())
    cheese = [tuple(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(N):
        if W > 0:
            if cheese[i][1] <= W:
                ans += cheese[i][0]
                W -= cheese[i][1]
            else:
                ans += cheese[i][0] * W / cheese[i][1]
                W = 0
    print(int(ans))

if __name__ == '__main__':
    main()