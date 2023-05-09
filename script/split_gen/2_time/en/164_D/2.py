def main():
    s = input()
    n = len(s)
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    ans = 0
    num = 0
    for i in range(n):
        num = (num + int(s[n - i - 1]) * pow(10, i, mod)) % mod
        cnt[num] += 1
    for i in range(mod):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
