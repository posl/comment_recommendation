def main():
    x = int(input())
    coin = [500, 100, 50, 10, 5, 1]
    ans = 0
    for i in range(6):
        ans += (x // coin[i]) * (coin[i] // 5) * 5
        x = x % coin[i]
    print(ans)

if __name__ == '__main__':
    main()