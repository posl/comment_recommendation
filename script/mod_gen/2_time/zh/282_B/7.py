def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()