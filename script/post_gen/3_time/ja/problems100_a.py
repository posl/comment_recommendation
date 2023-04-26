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
    a, b = map(int, input().split())
    if a <= 8 and b <= 8:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 4

def main():
    A,B=map(int,input().split())
    if A>8 or B>8:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 5

def main():
    # input
    a, b = map(int, input().split())

    # compute
    if a <= 8 and b <= 8:
        ans = "Yay!"
    else:
        ans = ":("

    # output
    print(ans)

=======
Suggestion 6

def main():
    # 標準入力から A, B を取得する
    A, B = map(int, input().split())

    # A+B が 16 以下であれば Yay! を返す
    if A+B <= 16:
        print("Yay!")
    else:
        print(":(")
