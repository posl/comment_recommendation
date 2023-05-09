def main():
    s = input()
    n = len(s)
    ans = 0
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    d = 1
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * d) % 2019
        d = (d * 10) % 2019
        cnt[t] += 1
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()