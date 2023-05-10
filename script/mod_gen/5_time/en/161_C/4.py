def main():
    n, k = map(int, input().split())
    ans = 0
    while n >= k:
        n = n % k
        ans = n
    print(min(ans, abs(ans-k)))

if __name__ == '__main__':
    main()