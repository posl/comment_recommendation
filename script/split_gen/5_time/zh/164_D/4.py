def main():
    s = input()
    s = s[::-1]
    n = len(s)
    mod = 2019
    cnt = [0]*mod
    cnt[0] = 1
    d = 1
    ans = 0
    for i in range(n):
        d = (d*10)%mod
        ans += cnt[d]
        cnt[d] += 1
    print(ans)
main()
