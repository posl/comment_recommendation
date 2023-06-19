Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    a,b,c = map(int,input().split())
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
    A, B, C = map(int, input().split())
    if (C == 0):
        if (A > B):
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if (A < B):
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 5

def solution():
    a,b,c = map(int, input().split())
    if (c == 0):
        if (a > b):
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if (b > a):
            print("Aoki")
        else:
            print("Takahashi")

solution()

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
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
    a,b,c = map(int,input().split())
    if a > b:
        print("Takahashi")
    elif a < b:
        print("Aoki")
    else:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 8

def main():
    # 读取数据
    a, b, c = map(int, input().split())
    # 判断谁先吃
    if c == 0:
        # 先吃的是高桥
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        # 先吃的是青木
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 9

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
Suggestion 10

def solve():
    A, B, C = map(int, input().split())

    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A < B:
            print("Aoki")
        else:
            print("Takahashi")
