def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += len(str(i))
    print(ans % 998244353)

if __name__ == '__main__':
    main()