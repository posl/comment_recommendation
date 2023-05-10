def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        s[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        ans += s[i] * (s[i] - 1) // 2
    for i in range(n):
        print(ans - s[a[i]] + 1)

if __name__ == '__main__':
    main()