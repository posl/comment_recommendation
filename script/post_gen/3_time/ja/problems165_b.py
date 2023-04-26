Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        money += money // 100
        year += 1
    print(year)

=======
Suggestion 2

def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        money = money * 101 // 100
        year += 1
    print(year)

=======
Suggestion 3

def main():
    X = int(input())
    money = 100
    year = 0
    while money < X:
        money = money + money // 100
        year += 1
    print(year)

=======
Suggestion 4

def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = y + y//100
        count += 1
    print(count)

=======
Suggestion 5

def main():
    x = int(input())
    n = 0
    while x > 100:
        x = x * 101 // 100
        n += 1
    print(n)

=======
Suggestion 6

def main():
    X = int(input())
    #print(X)
    year = 0
    money = 100
    while money < X:
        money = int(money * 1.01)
        year = year + 1
    print(year)

=======
Suggestion 7

def main():
    #入力
    X = int(input())
    #初期値
    year = 0
    money = 100
    #処理
    while money < X:
        money = int(money * 1.01)
        year += 1
    #出力
    print(year)

=======
Suggestion 8

def main():
    #入力
    X = int(input())
    #変数
    year = 0
    #処理
    while X > 100:
        X = int(X * 1.01)
        year += 1
    #出力
    print(year)

=======
Suggestion 9

def main():
    #入力
    X = int(input())
    #初期値
    Y = 100
    #処理
    for i in range(1, 10**10):
        Y = Y * 101 // 100
        if Y >= X:
            print(i)
            break
