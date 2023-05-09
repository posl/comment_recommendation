def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0] / x[1])
    ans = 0
    for i in range(N):
        if W == 0:
            break
        if W >= cheese[i][1]:
            W -= cheese[i][1]
            ans += cheese[i][0]
        else:
            ans += cheese[i][0] * (W / cheese[i][1])
            W = 0
    print(int(ans))

if __name__ == '__main__':
    main()