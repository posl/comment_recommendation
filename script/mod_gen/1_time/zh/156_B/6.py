def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        ans += 1
        n //= k
    print(ans)

if __name__ == '__main__':
    main()