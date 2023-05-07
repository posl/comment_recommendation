def main():
    N, K = map(int, input().split())
    # 3日目の合計点を計算
    points3 = [sum(map(int, input().split())) for _ in range(N)]
    # 4日目の合計点を計算
    points4 = [p + int(input()) for p in points3]
    # 3日目の合計点を降順にソート
    points3.sort(reverse=True)
    # 3日目の上位K人の合計点を求める
    top3 = points3[K - 1]
    # 4日目の合計点を降順にソート
    points4.sort(reverse=True)
    # 4日目の上位K人の合計点を求める
    top4 = points4[K - 1]
    # 3日目の上位K人の合計点が4日目の上位K人の合計点以上の場合は、
    # 4日目に全員が300点を取れば、4日目の上位K人の合計点は4日目の上位K人の合計点以上になる
    if top3 >= top4:
        print('Yes')
    else:
        print('No')
