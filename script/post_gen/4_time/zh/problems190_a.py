Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
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
    a,b,c = map(int, input().split())
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
    a,b,c = map(int,input().split())
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
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    elif C == 1:
        if A < B:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
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
Suggestion 6

def main():
    A,B,C = map(int,input().split())
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

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if b > a:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 9

def solve():
    A,B,C = map(int,input().split())

    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if A >= B:
            print('Takahashi')
        else:
            print('Aoki')
