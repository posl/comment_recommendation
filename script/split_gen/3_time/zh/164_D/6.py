def main():
    s = input()
    s = s[::-1]
    n = len(s)
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    num = 0
    ten = 1
    ans = 0
    for i in range(n):
        num += int(s[i]) * ten
        num %= mod
        ten = ten * 10 % mod
        ans += cnt[num]
        cnt[num] += 1
    print(ans)
