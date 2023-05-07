def main():
    n, d = map(int, input().split())
    ans = n // (2 * d + 1)
    if n % (2 * d + 1) != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()