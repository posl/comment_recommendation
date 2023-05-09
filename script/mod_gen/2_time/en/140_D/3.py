def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    ans += min(2 * k, n - 1)
    print(ans)

if __name__ == '__main__':
    main()