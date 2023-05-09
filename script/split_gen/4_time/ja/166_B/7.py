def main():
    # 標準入力の取得
    n, k = map(int, input().split())
    d = [0] * k
    a = [[] for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    # すぬけ君のお菓子の数を格納するリスト
    s = [0] * n
    for i in range(k):
        for j in range(d[i]):
            s[a[i][j]-1] += 1
    # お菓子を持っていないすぬけ君の数を数える
    count = 0
    for i in range(n):
        if s[i] == 0:
            count += 1
    # 結果の出力
    print(count)
