def main():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for i in range(n)]
    coins.sort(key=lambda x: x[0])
    for i in range(n):
        x -= coins[i][0] * coins[i][1]
        if x < 0:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()