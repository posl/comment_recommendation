Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    for s in S:
        print(s)

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    print(*S, sep='

')

=======
Suggestion 3

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 4

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    print('

'.join(S))

=======
Suggestion 5

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 6

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    T = [sorted(s, key=lambda x: X.index(x)) for s in S]
    for s, t in sorted(zip(S, T), key=lambda x: x[1]):
        print(s)

=======
Suggestion 7

def main():
    alphabet = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda x: [alphabet.index(c) for c in x])
    print(*S, sep='

')

=======
Suggestion 8

def main():
    #入力
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    #処理
    #アルファベット順に並べ替える
    S.sort(key=lambda x: [X.index(c) for c in x])

    #出力
    for i in range(N):
        print(S[i])

=======
Suggestion 9

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    # アルファベット順を辞書型で作成
    alphabet_dict = {}
    for i, alphabet in enumerate(X):
        alphabet_dict[alphabet] = i

    # アルファベットの値を辞書型で作成
    value_dict = {}
    for i, value in enumerate(sorted(alphabet_dict.values())):
        value_dict[value] = i

    # アルファベットを数値に変換
    S = [[value_dict[alphabet_dict[alphabet]] for alphabet in s] for s in S]

    # 数値をアルファベットに変換
    S = [[X[value] for value in s] for s in S]

    # アルファベットを辞書順に並び替え
    S.sort()

    # 数値をアルファベットに変換
    S = [[X[value] for value in s] for s in S]

    # アルファベットを文字列に変換
    S = [''.join(s) for s in S]

    for s in S:
        print(s)

=======
Suggestion 10

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #辞書順を定義する
    def comp(a, b):
        for i in range(min(len(a),len(b))):
            if X.index(a[i]) < X.index(b[i]):
                return -1
            elif X.index(a[i]) > X.index(b[i]):
                return 1
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        return 0
    #辞書順でソート
    S.sort(key=functools.cmp_to_key(comp))
    print(*S, sep='

')
