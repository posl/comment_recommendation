def main():
    s = input()
    n = len(s)
    a = [0] * n
    a[-1] = int(s[-1])
    for i in range(n-2, -1, -1):
        a[i] = (int(s[i]) * pow(10, n-i-1) + a[i+1]) % 2019
    b = [0] * 2019
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2019):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()