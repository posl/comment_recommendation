def solve():
    N, X = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(N)]
    coins = sorted(coins, key=lambda x: x[0])
    total = 0
    for i in range(N):
        total += coins[i][0] * coins[i][1]
        if total > X:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()