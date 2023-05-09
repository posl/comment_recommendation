def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        ans += i * (i - 1) // 2
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, n + 1):
        ans -= c[i] * (c[i] - 1) // 2
    print(ans)
main()

if __name__ == '__main__':
    main()