def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if n <= k:
            break
        n -= k
        ans += 1
    print(ans + 1)

if __name__ == '__main__':
    main()