def main():
    n, k = map(int, input().split())
    s = list(input())
    cnt = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            cnt += 1
    ans = min(n - 1, cnt + 2 * k)
    print(ans)

if __name__ == '__main__':
    main()