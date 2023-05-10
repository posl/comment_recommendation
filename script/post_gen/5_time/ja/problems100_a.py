Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 2

def main():
    #1行目の入力を取得
    a,b = map(int,input().split())
    #A+Bが16以下かどうか
    if a+b <= 16:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A <= 8 and B <= 8:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if (a>8 or b>8):
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A > 8 or B > 8:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 6

def problem100_a():
    a,b = map(int,input().split())
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")
