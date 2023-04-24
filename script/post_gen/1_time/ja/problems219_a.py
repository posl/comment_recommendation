Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print('expert')

=======
Suggestion 2

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print("expert")

=======
Suggestion 3

def main():
    X = int(input())
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("expert")

=======
Suggestion 4

def main():
    # 入力
    X = int(input())

    # 出力
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("expert")

=======
Suggestion 5

def main():
    #入力
    X = int(input())
    #処理
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("expert")

=======
Suggestion 6

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    else:
        print(40 * ((x // 40) + 1) - x)

=======
Suggestion 7

def main():
    # 0 ≦ X ≦ 100
    # X は整数
    X = int(input())
    if X == 100:
        print("expert")
    elif X >= 90:
        print(100 - X)
    elif X >= 70:
        print(90 - X)
    elif X >= 40:
        print(70 - X)
    else:
        print(40 - X)
