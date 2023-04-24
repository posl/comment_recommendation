Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S == "SUN":
        print(7)
    elif S == "MON":
        print(6)
    elif S == "TUE":
        print(5)
    elif S == "WED":
        print(4)
    elif S == "THU":
        print(3)
    elif S == "FRI":
        print(2)
    elif S == "SAT":
        print(1)

=======
Suggestion 2

def main():
    s = input()
    if s == "SUN":
        print(7)
    if s == "MON":
        print(6)
    if s == "TUE":
        print(5)
    if s == "WED":
        print(4)
    if s == "THU":
        print(3)
    if s == "FRI":
        print(2)
    if s == "SAT":
        print(1)

=======
Suggestion 3

def main():
    x = input()
    if x == 'SUN':
        print(7)
    elif x == 'MON':
        print(6)
    elif x == 'TUE':
        print(5)
    elif x == 'WED':
        print(4)
    elif x == 'THU':
        print(3)
    elif x == 'FRI':
        print(2)
    elif x == 'SAT':
        print(1)

=======
Suggestion 4

def main():
    #入力
    S = input()

    #出力
    if S == "SUN":
        print(7)
    elif S == "MON":
        print(6)
    elif S == "TUE":
        print(5)
    elif S == "WED":
        print(4)
    elif S == "THU":
        print(3)
    elif S == "FRI":
        print(2)
    elif S == "SAT":
        print(1)

=======
Suggestion 5

def main():
    # 文字列の入力
    s = input()
    # 出力
    if s == "SUN":
        print(7)
    elif s == "MON":
        print(6)
    elif s == "TUE":
        print(5)
    elif s == "WED":
        print(4)
    elif s == "THU":
        print(3)
    elif s == "FRI":
        print(2)
    elif s == "SAT":
        print(1)
    else:
        print("Error")

=======
Suggestion 6

def main():
    day = input()
    day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - day_list.index(day))

=======
Suggestion 7

def main():
    #入力
    S = input()
    
    #処理
    if S == "SUN":
        ans = 7
    elif S == "MON":
        ans = 6
    elif S == "TUE":
        ans = 5
    elif S == "WED":
        ans = 4
    elif S == "THU":
        ans = 3
    elif S == "FRI":
        ans = 2
    elif S == "SAT":
        ans = 1
    
    #出力
    print(ans)

main()

=======
Suggestion 8

def main():
    # 標準入力から1行取得
    s = input()

    # 条件分岐
    if s == 'SUN':
        print(7)
    elif s == 'MON':
        print(6)
    elif s == 'TUE':
        print(5)
    elif s == 'WED':
        print(4)
    elif s == 'THU':
        print(3)
    elif s == 'FRI':
        print(2)
    elif s == 'SAT':
        print(1)

=======
Suggestion 9

def main():
    # 標準入力から読み込み
    s = input()
    # 標準出力に出力
    print(7 - ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"].index(s))

=======
Suggestion 10

def main():
    # 標準入力から1行を取得
    s = input()
    # 辞書型で曜日を定義
    week = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    # 辞書型で定義した曜日の値を取得
    value = week[s]
    # 今日が日曜日の場合は7日後、それ以外は7 - 今日の曜日の値
    if value == 0:
        print(7)
    else:
        print(7 - value)
