Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    t = [a, b, c, d, e]
    t.sort()
    ans = 0
    for i in range(4):
        if t[i] % 10 != 0:
            ans += (t[i] // 10 + 1) * 10
        else:
            ans += t[i]
    ans += t[4]
    print(ans)

=======
Suggestion 2

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    t = [A, B, C, D, E]
    t.sort()
    print((t[0] + 9) // 10 * 10 + t[1] + t[2] + t[3] + t[4])

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a, b, c, d, e]
    time.sort()
    if time[4] % 10 == 0:
        print(time[4] * 4)
    else:
        print(time[4] // 10 * 10 * 4 + 10 * 4)

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = [A, B, C, D, E]
    time.sort()
    print(10 * (len(time) - 1) + time[-1])

=======
Suggestion 5

def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print((A + 9) // 10 * 10 + (B + 9) // 10 * 10 + (C + 9) // 10 * 10 + (D + 9) // 10 * 10 + E - max(A, B, C, D, E) + 9)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((a-1)//10*10+10+(b-1)//10*10+10+(c-1)//10*10+10+(d-1)//10*10+10+(e-1)//10*10+10)

=======
Suggestion 7

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    order_time = 0
    order_list = [A, B, C, D, E]
    order_list.sort()
    for i in range(0, 5):
        if order_time % 10 != 0:
            order_time += 10 - order_time % 10
        order_time += order_list[i]
    print(order_time)

=======
Suggestion 8

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A, B, C, D, E)
    
    #料理の調理時間をリストに格納
    cook_time = [A, B, C, D, E]
    #料理の調理時間を昇順にソート
    cook_time.sort()
    #print(cook_time)
    
    #料理の調理時間が最小の料理の調理時間を取得
    min_cook_time = cook_time[0]
    #print(min_cook_time)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った余りを取得
    #余りが 0 でなければ、料理の調理時間が最小の料理の調理時間を 10 で割った商に 1 を足した値を取得
    if min_cook_time % 10 == 0:
        min_cook_time_10 = min_cook_time // 10
    else:
        min_cook_time_10 = min_cook_time // 10 + 1
    #print(min_cook_time_10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値を取得
    #print(min_cook_time_10 * 10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値を最も早く注文できる時刻とする
    #print(min_cook_time_10 * 10)
    
    #料理の調理時間が最小の料理の調理時間を 10 で割った商に 10 を掛けた値 + 料理の調理時間が最大の料理の調理時間を取得

=======
Suggestion 9

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A,B,C,D,E)
    a = (A+9)//10*10
    b = (B+9)//10*10
    c = (C+9)//10*10
    d = (D+9)//10*10
    e = (E+9)//10*10
    #print(a,b,c,d,e)
    f = min(a,b,c,d,e)
    #print(f)
    if f == a:
        print(a+A)
    elif f == b:
        print(b+B)
    elif f == c:
        print(c+C)
    elif f == d:
        print(d+D)
    elif f == e:
        print(e+E)

=======
Suggestion 10

def main():
    # 入力
    A=int(input())
    B=int(input())
    C=int(input())
    D=int(input())
    E=int(input())
    # 処理
    # ABC 丼→ARC カレー→AGC パスタ→ATC ハンバーグ→APC ラーメンの順に注文することにする
    # 時刻 0 に ABC 丼を注文する。時刻 29 に ABC 丼が届く。
    # 時刻 30 に ARC カレーを注文する。時刻 50 に ARC カレーが届く。
    # 時刻 50 に AGC パスタを注文する。57 に AGC パスタが届く。
    # 時刻 60 に ATC ハンバーグを注文する。時刻 180 に ATC ハンバーグが届く。
    # 時刻 180 に APC ラーメンを注文する。時刻 215 に APC ラーメンが届く。
    # 時刻 215 に ABC 丼を注文する。時刻 244 に ABC 丼が届く。
    # 時刻 245 に ARC カレーを注文する。時刻 265 に ARC カレーが届く。
    # 時刻 265 に AGC パスタを注文する。時刻 272 に AGC パスタが届く。
    # 時刻 280 に ATC ハンバーグを注文する。時刻 400 に ATC ハンバーグが届く。
    # 時刻 400 に APC ラーメンを注文する。時刻 435 に APC ラーメンが届く。
    # 時刻 435 に ABC 丼を注文する。時刻 464 に ABC 丼が
