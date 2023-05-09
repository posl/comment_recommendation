def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    # 0 から 9 までの個数を数える
    cnt = [0] * 10
    for a in A:
        cnt[a] += 1
    # 0 から 9 までの個数の累積和をとる
    cum = [0] * 11
    for i in range(10):
        cum[i + 1] = cum[i] + cnt[i]
    # 操作 F と操作 G の両方を試す
    for k in range(10):
        res = 1
        for i in range(10):
            # 操作 F で削除される個数
            n1 = cum[min(i + k, 10)] - cum[i]
            # 操作 G で削除される個数
            n2 = cum[min(i * k % 10 + 10, 10)] - cum[i * k % 10]
            # 両方の操作で削除される個数
            n = n1 + n2
            res = res * pow(2, n, mod) % mod
        print(res)
main()

if __name__ == '__main__':
    main()