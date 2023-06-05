def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (n + 1)
    for i in range(n):
        l[a[i]] = i
    r = [0] * (n + 1)
    for i in range(n):
        r[a[i]] = i
    ans = 0
    for i in range(1, n + 1):
        ans += (l[i] - l[i - 1]) * (r[i] - r[i - 1])
    print(ans)

if __name__ == '__main__':
    main()