Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a < b:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a >= b:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a >= b:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print("Takahashi" if a > b or (a == b and c == 0) else "Aoki")

=======
Suggestion 6

def main():
    # 標準入力から A, B, C を取得する
    A, B, C = map(int, input().split())
    # ここにプログラムを追記
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if B > A:
            print('Aoki')
        else:
            print('Takahashi')
