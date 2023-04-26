Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 2

def main():
    S = input()
    if S <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    S = input()
    S = S.split("/")
    if int(S[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 5

def main():
    #S = input()
    S = "2019/11/01"
    #print(S)
    S = S.split("/")
    #print(S)
    if int(S[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 6

def main():
    # 文字列 S が入力されます。
    S = input()
    # 2019/04/30 = 20190430
    # 2019/11/01 = 20191101
    # 2019/04/30 以降の場合は、S が表す日付が 2019 年 4 月 30 日以降なら TBD、そうでなければ Heisei と出力するプログラムを書いてください。
    if int(S.replace('/', '')) <= 20190430:
        print('Heisei')
    else:
        print('TBD')
