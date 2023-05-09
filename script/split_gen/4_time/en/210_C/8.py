def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    # すでに見た色を保存するためのリスト
    seen = []
    # 今見ている連続するk個の色
    tmp = c[:k]
    # 今見ている連続するk個の色の中で最も多く出現する色の数
    ans = 0
    for i in range(k):
        if tmp[i] not in seen:
            seen.append(tmp[i])
            ans = max(ans, len(seen))
    for i in range(k, n):
        # 今見ている連続するk個の色の中で最も多く出現する色の数
        # 重複を許しているので、最大値はk
        if ans == k:
            break
        # 一番左の色を除く
        tmp = tmp[1:]
        # 新しく追加する色
        new_c = c[i]
        # 除いた色が新しく追加する色と違う場合
        if new_c not in tmp:
            # 除いた色がすでに見た色にある場合
            if new_c in seen:
                # 除いた色を新しく追加する色に置き換える
                tmp.append(new_c)
            # 除いた色がすでに見た色にない場合
            else:
                # 除いた色を新しく追加する色に置き換える
                tmp.append(new_c)
                # 除いた色を新しく追加する色に置き換えたので、
                # 今見ている連続するk個の色の中で最も多く出現する色の数を更新する
                ans = max(ans, len(seen) + 1)
        # 一番左の色を除いた場合、
        # 今見ている連続するk個
