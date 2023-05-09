def main():
    n, x, t = map(int, input().split())
    ans = 0
    while n > 0:
        ans += t
        n -= x
    print(ans)

if __name__ == '__main__':
    main()