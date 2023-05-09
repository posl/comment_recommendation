def main():
    S = input()
    mod = 10**9 + 7
    ans = 1
    cnt = [0] * 8
    for s in S:
        if s == 'c':
            cnt[0] += 1
        elif s == 'h':
            cnt[1] += cnt[0]
        elif s == 'o':
            cnt[2] += cnt[1]
        elif s == 'k':
            cnt[3] += cnt[2]
        elif s == 'u':
            cnt[4] += cnt[3]
        elif s == 'd':
            cnt[5] += cnt[4]
        elif s == 'a':
            cnt[6] += cnt[5]
        elif s == 'i':
            cnt[7] += cnt[6]
    print(cnt[7] % mod)
