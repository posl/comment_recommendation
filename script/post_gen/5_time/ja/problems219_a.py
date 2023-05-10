Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    elif x >= 90 and x <= 100:
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
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    else:
        print('expert')

=======
Suggestion 4

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    elif x >= 70:
        print(90 - x)
    elif x >= 40:
        print(70 - x)
    else:
        print(40 - x)

=======
Suggestion 5

def Rank(x):
    if x >= 0 and x < 40:
        return 40 - x
    elif x >= 40 and x < 70:
        return 70 - x
    elif x >= 70 and x < 90:
        return 90 - x
    elif x >= 90 and x <= 100:
        return "expert"
    else:
        return "error"

=======
Suggestion 6

def problem219_a():
    #入力
    X = int(input())
    #処理
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    elif X >= 90 and X <= 100:
        print('expert')
    else:
        print('入力された値が不正です。')

problem219_a()

=======
Suggestion 7

def main():
    x = int(input())
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    else:
        print("expert")

=======
Suggestion 8

def main():
    # input
    x = int(input())
    # compute
    if x < 40:
        print(40-x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print('expert')
    # output
