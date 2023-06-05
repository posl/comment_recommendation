def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(n):
        ans = max(ans, s[i + 1])
    print(ans)

if __name__ == '__main__':
    main()