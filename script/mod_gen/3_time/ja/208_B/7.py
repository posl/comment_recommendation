def main():
    p = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[i-2]*i)
    coin.reverse()
    ans = 0
    for c in coin:
        ans += p//c
        p %= c
    print(ans)

if __name__ == '__main__':
    main()