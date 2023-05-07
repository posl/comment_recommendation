def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    # 重複を削除したSを作成
    S_set = list(set(S))
    # 重複を削除したSの要素数を取得
    S_set_len = len(S_set)
    # 重複を削除したSの要素数分だけループ
    for i in range(S_set_len):
        # 重複を削除したSの要素を取得
        S_set_i = S_set[i]
        # 同じ要素のインデックスを取得
        S_set_i_index = [j for j, x in enumerate(S) if x == S_set_i]
        # 同じ要素のインデックスの要素数を取得
        S_set_i_index_len = len(S_set_i_index)
        # 同じ要素のインデックスの要素数が1の場合は最優秀賞
        if S_set_i_index_len == 1:
            # 最優秀賞のインデックスを取得
            best_index = S_set_i_index[0]
            # 最優秀賞のインデックス+1を出力
            print(best_index+1)
            break
        # 同じ要素のインデックスの要素数が1より大きい場合は最優秀賞を探す
        else:
            # 同じ要素のインデックスの要素数分だけループ
            for j in range(S_set_i_index_len):
                # 同じ要素のインデックスを取得
                S_set_i_index_j = S_set_i_index[j]
                # 同じ要素のインデックスの要素数分だけループ
                for k in range(S_set_i_index_len):
                    # 同じ要素のインデックスを取得
                    S_set_i_index_k
