def solve(n, k, p):
    # 1日目の点数を基準にソート
    p.sort(key=lambda x: x[0], reverse=True)
    # 1日目の点数の順位
    rank = [0] * n
    # 1日目の点数の順位を計算
    for i in range(n):
        if i != 0 and p[i][0] != p[i - 1][0]:
            rank[i] = rank[i - 1] + 1
        else:
            rank[i] = rank[i - 1]
    # 4日目の点数の上位K人の最低点数
    min_4th = p[k - 1][0] + p[k - 1][1] + p[k - 1][2]
    # 3日目までの点数を基準にソート
    p.sort(key=lambda x: x[1] + x[2], reverse=True)
    # 3日目までの点数の順位
    rank3 = [0] * n
    # 3日目までの点数の順位を計算
    for i in range(n):
        if i != 0 and p[i][1] + p[i][2] != p[i - 1][1] + p[i - 1][2]:
            rank3[i] = rank3[i - 1] + 1
        else:
            rank3[i] = rank3[i - 1]
    # 3日目までの点数の順位と1日目の点数の順位を合わせた順位
    rank4 = [0] * n
    for i in range(n):
        rank4[i] = rank[i] + rank3[i]
    # 3日目までの点数の合計がmin_4thを超える場合は4日目の点数で上位K人に入ることができる
    for i in range(n):
        if p[i][1] + p[i][2] >= min_4th:
            print("Yes")
        else:
            # 4
