def main():
    N = int(input())
    # 頂点の数を取得
    a = []
    b = []
    for i in range(N-1):
        # 辺の数だけループ
        a_i, b_i = map(int, input().split())
        # 辺の両端を取得
        a.append(a_i)
        b.append(b_i)
    # 答えを格納する変数
    ans = "Yes"
    for i in range(N-1):
        # 辺の数だけループ
        if a.count(a[i]) == 1:
            # a[i]が1個しかない場合
            if b.count(a[i]) == N-1:
                # a[i]がN-1個ある場合
                continue
            else:
                # a[i]がN-1個ある場合以外
                ans = "No"
                break
        elif b.count(a[i]) == 1:
            # b[i]が1個しかない場合
            if a.count(a[i]) == N-1:
                # a[i]がN-1個ある場合
                continue
            else:
                # a[i]がN-1個ある場合以外
                ans = "No"
                break
        else:
            # a[i]とb[i]が1個しかない場合以外
            ans = "No"
            break
    print(ans)
