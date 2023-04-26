Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 2

def main():
    # A, B, C, D, E = map(int, input().split())
    # print(len(set([A, B, C, D, E])))
    print(len(set(map(int, input().split()))))

=======
Suggestion 3

def main():
    #入力
    A, B, C, D, E = map(int, input().split())
    #出力
    print(len(set([A, B, C, D, E])))

=======
Suggestion 4

def main():
    #入力
    a, b, c, d, e = map(int, input().split())
    #出力
    print(len(set([a, b, c, d, e])))

=======
Suggestion 5

def main():
    # 自分の得意な言語で
    # Let's チャレンジ！！

    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 6

def main():
    # 入力
    a, b, c, d, e = map(int, input().split())
    # 処理
    set_a = set([a, b, c, d, e])
    # 出力
    print(len(set_a))

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 8

def main():
    #入力
    a, b, c, d, e = map(int, input().split())
    #処理
    #set関数を用いて、重複する値を取り除く
    #len関数を用いて、要素数を数える
    #出力
    print(len(set([a, b, c, d, e])))
