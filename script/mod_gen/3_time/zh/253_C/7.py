def main():
    import sys
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    def input(): return sys.stdin.readline().rstrip()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    # 値と出現回数を記録する辞書
    value_dict = defaultdict(int)
    # 値のリスト
    value_list = []
    # 値のリストをソート済みに保つためのリスト
    value_list_sorted = []
    # 値のリストの中で、値が何番目に小さいかを管理する辞書
    value_to_index = {}
    # 値のリストの中で、値が何番目に大きいかを管理する辞書
    value_to_index_rev = {}
    # 値のリストに値を追加する
    def add_value(x):
        value_dict[x] += 1
        value_list.append(x)
        value_list_sorted.append(x)
        # 値のリストをソート
        value_list_sorted.sort()
        # 値のリストの中で、値が何番目に小さいかを管理する辞書を更新
        value_to_index[x] = bisect_left(value_list_sorted, x)
        # 値のリストの中で、値が何番目に大きいかを管理する辞書を更新
        value_to_index_rev[x] = bisect_right(value_list_sorted, x) - 1
    # 値のリストから値を削除する
    def remove_value(x):
        value_dict[x] -= 1
        value_list.remove(x)
        # 値のリストの中で、値が何番目に小さいかを管理する辞書を更新
        value_to_index[x] = bisect_left(value_list_sorted, x)
        # 値のリストの中で、値が何番目に大きいかを管理する辞書を更新
        value_to_index_rev[x] = bis

if __name__ == '__main__':
    main()