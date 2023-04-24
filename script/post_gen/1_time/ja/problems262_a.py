Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1

=======
Suggestion 2

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 3

def main():
    y = int(input())
    if y % 4 == 2:
        print(y)
    else:
        print(y + (4 - y % 4))

=======
Suggestion 4

def main():
    y = int(input())
    while y % 4 != 2:
        y += 1
    print(y)

=======
Suggestion 5

def main():
    Y = int(input())
    while Y % 4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 6

def main():
    y = int(input())
    ans = y
    while ans % 4 != 2:
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    #入力
    y = int(input())

    #処理
    #西暦年を 4 で割った余りが 2 である年の 6 月に開催されます。
    #y = y + 2
    #if y % 4 == 0:
    #    y = y + 2
    #else:
    #    y = y + 4

    #y = y + (4 - y % 4)
    #y = y + (4 - y % 4) if y % 4 != 0 else y + 2

    #y = y + (4 - y % 4) if y % 4 != 0 else y + 2
    y = y + (4 - y % 4) if y % 4 != 0 else y + 2

    #出力
    print(y)

=======
Suggestion 8

def main():
    Y = int(input())
    if Y%4 == 0:
        print(Y)
    else:
        print(Y + (4 - Y%4))

=======
Suggestion 9

def main():
    y = int(input())
    print(y + 2 - y % 4)
