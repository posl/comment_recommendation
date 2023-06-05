def main():
    n, m = map(int, input().split())
    s = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        if a == 1:
            s[b] = 1
        elif b == n:
            s[a] = 1
    ans = 0
    for i in range(2, n):
        if s[i] == 1 and s[i + 1] == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()