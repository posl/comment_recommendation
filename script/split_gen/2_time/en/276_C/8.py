def main():
    n = int(input())
    p = list(map(int, input().split()))
    # 1. pを逆順に見ていき、最初に見つけたa[i] < a[i-1]となるiを見つける
    # 2. p[:i-1] + p[i:]のうち、p[i:]の中でp[i-1]より大きく、かつ最小の値をp[i-1]とする
    # 3. p[:i]を昇順にソートする
    # 4. p[:i] + p[i:]を出力する
    for i in range(n - 1, 0, -1):
        if p[i] > p[i - 1]:
            break
    else:
        print(-1)
        return
    for j in range(n - 1, i - 1, -1):
        if p[j] > p[i - 1]:
            p[i - 1], p[j] = p[j], p[i - 1]
            break
    p[:i] = sorted(p[:i])
    print(' '.join(map(str, p)))
