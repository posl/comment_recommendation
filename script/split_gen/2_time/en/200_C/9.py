def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200で割った余りをキーとして、その余りの数を値とする辞書を作成
    d = {}
    for i in range(n):
        r = a[i] % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    # 余りの数が2以上のものを抜き出し、それらの組み合わせの数を計算
    ans = 0
    for k, v in d.items():
        if v >= 2:
            ans += v * (v - 1) // 2
    print(ans)
