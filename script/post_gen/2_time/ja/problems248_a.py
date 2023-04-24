Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 2

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            return

=======
Suggestion 3

def main():
    S = input()
    for i in range(10):
        if str(i) not in S:
            print(i)
            break

=======
Suggestion 4

def main():
    s = input()
    for i in range(10):
        if s.count(str(i)) == 0:
            print(i)

=======
Suggestion 5

def main():
    s = input()
    s = set(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            return

=======
Suggestion 6

def main():
    s = input()
    s = list(map(int, s))
    for i in range(10):
        if i not in s:
            print(i)
            return

=======
Suggestion 7

def main():
    s = input()
    s = list(s)
    s.sort()
    for i in range(9):
        if s[i] == str(i):
            continue
        else:
            print(i)
            break

=======
Suggestion 8

def main():
    s = input()
    s = list(s)
    s.sort()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 9

def main():
    #入力
    s = input()
    #文字列をリストにする
    s_list = list(s)
    #文字列の要素を数値に変換
    s_list = [int(i) for i in s_list]
    #0~9のリストを作成
    ten_list = [i for i in range(10)]
    #リストの差集合をとる
    ans = set(ten_list) - set(s_list)
    #集合をリストに変換
    ans = list(ans)
    #リストを文字列に変換
    ans = str(ans[0])
    #出力
    print(ans)
