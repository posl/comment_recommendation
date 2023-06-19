def main():
    #读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #计算前缀和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    #计算余数的个数
    cnt = {}
    for i in range(n + 1):
        r = s[i] % m
        if r not in cnt:
            cnt[r] = 0
        cnt[r] += 1
    #计算答案
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()