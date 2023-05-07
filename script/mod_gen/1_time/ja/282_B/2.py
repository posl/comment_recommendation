def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if 'o' in s[i] or 'o' in s[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()