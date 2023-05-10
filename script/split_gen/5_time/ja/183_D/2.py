def main():
    n, w = map(int, input().split())
    s = [0] * n
    t = [0] * n
    p = [0] * n
    for i in range(n):
        s[i], t[i], p[i] = map(int, input().split())
    #print(s)
    #print(t)
    #print(p)
    # 各時刻でのお湯の使用量
    use = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        use[s[i]] += p[i]
        use[t[i]] -= p[i]
    #print(use)
    # 各時刻でのお湯の使用量の累積和
    use_cum = [0] * (2 * 10 ** 5 + 1)
    for i in range(2 * 10 ** 5):
        use_cum[i + 1] = use_cum[i] + use[i]
    #print(use_cum)
    # お湯の使用量が W を超えているかどうか
    for i in range(2 * 10 ** 5):
        if use_cum[i] > w:
            print('No')
            return
    print('Yes')
