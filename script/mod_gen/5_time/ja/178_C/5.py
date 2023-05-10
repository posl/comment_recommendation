def main():
    n = int(input())
    ans = 1
    for i in range(n):
        ans *= 10
        ans %= 1000000007
    ans -= 2
    ans += 1000000007
    ans %= 1000000007
    for i in range(n):
        ans *= 9
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()