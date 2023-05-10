def main():
    n, x = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(list(map(int, input().split())))
    total = 0
    for i in range(n):
        total += coins[i][0] * coins[i][1]
    if total <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()