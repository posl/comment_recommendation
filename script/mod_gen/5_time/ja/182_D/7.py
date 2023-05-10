def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    maxs = [0] * (n + 1)
    for i in range(n):
        maxs[i + 1] = max(maxs[i], s[i + 1])
    ans = 0
    x = 0
    for i in range(n):
        ans = max(ans, x + maxs[i + 1])
        x += s[i + 1]
    print(ans)

if __name__ == '__main__':
    main()