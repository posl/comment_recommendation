def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + b[i + 1]
    ans = 0
    for i in range(n):
        ans += c[n] - c[i] - (b[i + 1] * (n - i))
    print(ans // n)

if __name__ == '__main__':
    main()