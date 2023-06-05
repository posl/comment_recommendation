def main():
    s = input()
    n = len(s)
    a = [0]*2019
    a[0] = 1
    t = 0
    ans = 0
    for i in range(n-1, -1, -1):
        t += int(s[i])*pow(10, n-1-i, 2019)
        t %= 2019
        ans += a[t]
        a[t] += 1
    print(ans)

if __name__ == '__main__':
    main()