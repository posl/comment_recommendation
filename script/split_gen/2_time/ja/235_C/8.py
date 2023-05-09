def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    xk = [list(map(int, input().split())) for _ in range(q)]
    # aの要素をキーとする辞書を作成
    # 辞書の値は、そのキーの値がaで出現するインデックスのリスト
    d = {}
    for i, v in enumerate(a):
        if v in d:
            d[v].append(i+1)
        else:
            d[v] = [i+1]
    for x, k in xk:
        if x in d:
            if k <= len(d[x]):
                print(d[x][k-1])
            else:
                print(-1)
        else:
            print(-1)
