def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()