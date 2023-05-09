def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    ans += (n - 1) // (k - 1)
    if (n - 1) % (k - 1) != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()