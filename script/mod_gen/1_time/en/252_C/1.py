def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        cnt = [0] * 10
        for j in range(n):
            cnt[int(s[j][i])] += 1
        ans += max(cnt) * 10 ** (9 - i)
    print(ans)
main()
