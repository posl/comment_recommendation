def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (n + 1)
    for i in range(n):
        if i == 0:
            b[i] = 1
            continue
        if a[i] == a[i - 1]:
            b[i] = b[i - 1] + 1
        else:
            b[i] = 1
    ans = 0
    for i in range(n):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        if a[i] != a[i - 1]:
            continue
        ans -= (b[i] - 1) * (b[i] - 2) // 2
    for i in range(n):
        if a[i] == a[i - 1]:
            continue
        ans -= (b[i] - 1) * (b[i] - 2) // 2
    print(ans)

if __name__ == '__main__':
    main()