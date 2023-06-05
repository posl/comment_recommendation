def main():
    s = input()
    n = len(s)
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    p = 1
    for i in range(n - 1, -1, -1):
        t = (t + int(s[i]) * p) % 2019
        p = p * 10 % 2019
        cnt[t] += 1
    ans = 0
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()