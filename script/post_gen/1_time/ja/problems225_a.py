Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print(3)
    else:
        print(6)

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print(3)
    else:
        print(6)

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[0] == S[2] or S[1] == S[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 4

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 5

def main():
    # 文字列Sを取得
    S = input()
    # 文字列Sの文字をリスト化
    S_list = list(S)
    # 文字列Sの文字をソート
    S_list.sort()
    # 文字列Sの文字をソートしたリストを文字列に変換
    S_sort = ''.join(S_list)
    # 文字列Sの文字をソートしたリストをsetに変換
    S_set = set(S_sort)
    # setの長さを出力
    print(len(S_set))

=======
Suggestion 6

def main():
    # 文字列を入力
    S = input()
    # abcの順列を作成
    abc = list(itertools.permutations('abc', 3))
    # 文字列をリストに変換
    S = list(S)
    # 文字列をリストに変換
    S = list(S)
    # abcの順列のリストをループ
    for i in abc:
        # 文字列のリストとabcの順列のリストを比較
        if S == list(i):
            # 一致したら出力
            print(abc.index(i)+1)
