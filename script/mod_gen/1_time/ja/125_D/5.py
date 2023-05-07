def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += abs(a[i])
    ans += abs(a[0])
    ans += abs(a[-1])
    for i in range(n - 1):
        ans -= max(abs(a[i] - a[i + 1]), abs(a[i]) + abs(a[i + 1]))
    print(ans)

if __name__ == '__main__':
    main()