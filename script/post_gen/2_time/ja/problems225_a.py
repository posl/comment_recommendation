Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
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
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[0] == S[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(1)
        else:
            print(2)
    elif S[0] == S[2]:
        print(2)
    elif S[1] == S[2]:
        print(2)
    else:
        print(3)

=======
Suggestion 5

def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print(3)
        else:
            print(6)
    else:
        print("length error")

=======
Suggestion 6

def main():
    S = input()
    x = len(set(S))
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        print(6)

=======
Suggestion 7

def main():
    # 1行目の入力
    s = input()
    # 2行目の入力
    #n = int(input())
    # 3行目以降の入力
    #a = list(map(int, input().split()))
    # 1行目の出力
    print(len(set(s)))

=======
Suggestion 8

def main():
    #入力
    S = input()
    #文字列をリストに変換
    S = list(S)
    #重複を削除
    S = list(set(S))
    #文字列の長さを取得
    length = len(S)
    #出力
    print(length)
    #出力例 1
    #3
    #出力例 2
    #1
    #出力例 3
    #6

=======
Suggestion 9

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 10

def main():
    s = input()
    # setに変換して重複を削除
    s = set(s)
    # setをリストに変換して長さを出力
    print(len(s))
