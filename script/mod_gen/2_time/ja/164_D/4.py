def main():
    S = input()
    S = S[::-1]
    ans = 0
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    d = 1
    now = 0
    for s in S:
        now += int(s) * d
        now %= mod
        d *= 10
        d %= mod
        ans += cnt[now]
        cnt[now] += 1
    print(ans)

if __name__ == '__main__':
    main()