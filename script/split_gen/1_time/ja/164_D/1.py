def main():
    s = input()
    n = len(s)
    ans = 0
    cnt = [0] * 2019
    cnt[0] = 1
    d = 1
    for i in range(n - 1, -1, -1):
        ans += cnt[d * int(s[i]) % 2019]
        cnt[d * int(s[i]) % 2019] += 1
        d = d * 10 % 2019
    print(ans)
