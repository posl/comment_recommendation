def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    # print(N)
    # print(S)
    # print(T)
    # print()
    # print()
    # print()
    # 一番最初の提出の得点
    max_score = max(T)
    # print(max_score)
    # 一番最初の提出の得点のインデックス
    max_score_index = T.index(max_score)
    # print(max_score_index)
    # 一番最初の提出の文字列
    max_score_string = S[max_score_index]
    # print(max_score_string)
    # 一番最初の提出の文字列のインデックス
    max_score_string_index = S.index(max_score_string)
    # print(max_score_string_index)
    # 一番最初の提出の文字列の得点
    max_score_string_score = T[max_score_string_index]
    # print(max_score_string_score)
    # 一番最初の提出の文字列の得点のインデックス
    max_score_string_score_index = T.index(max_score_string_score)
    # print(max_score_string_score_index)
    # 一番最初の提出の文字列の得点のインデックスが一番最初の提出のインデックスと一致していたら、一番最初の提出が最優秀賞
    if max_score_string_score_index == max_score_index:
        print(max_score_string_score_index+1)
    # 一番最初の提出の文字列の得点のインデックスが一番最初の提出のインデックスと一致していなかったら、一番最初の提出が最優秀賞ではない
    else:
        print(max_score_string_score_index+1)

if __name__ == '__main__':
    main()