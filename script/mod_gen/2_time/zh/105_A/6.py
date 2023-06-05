def main():
    n, k = map(int, input().split())
    ans = 0
    if n % k != 0:
        ans = 1
    print(ans)

if __name__ == '__main__':
    main()