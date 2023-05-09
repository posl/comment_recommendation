def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(2, m+1):
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        ans *= cnt + 1
        ans %= 10**9 + 7
    print(ans)

if __name__ == '__main__':
    main()