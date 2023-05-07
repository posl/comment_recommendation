def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        if s[i][-3:] in t:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()