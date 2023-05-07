def main():
    # 食品の数と嫌いな食品の数
    n, k = map(int, input().split())
    # 食品のおいしさ
    a = list(map(int, input().split()))
    # 嫌いな食品
    b = list(map(int, input().split()))
    # 食品のおいしさが最大の食品
    max_a = max(a)
    # 食品のおいしさが最大の食品のインデックス
    max_a_index = a.index(max_a)
    # 食品のおいしさが最大の食品のインデックスが嫌いな食品のリストに含まれるか
    if max_a_index + 1 in b:
        print('Yes')
    else:
        print('No')
