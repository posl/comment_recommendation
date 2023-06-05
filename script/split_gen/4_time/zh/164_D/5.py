def main():
    s = input()
    n = len(s)
    mod = 2019
    ans = 0
    cnt = [0] * mod
    cnt[0] = 1
    t = 0
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * pow(10, i, mod)) % mod
        ans += cnt[t]
        cnt[t] += 1
    print(ans)
