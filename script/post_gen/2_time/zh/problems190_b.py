Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a < b:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 2

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
Suggestion 3

def main():
    a,b,c = map(int,input().split())
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
Suggestion 4

def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 处理数据
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
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        elif a < b:
            print("Aoki")
        else:
            print("Aoki")
    else:
        if a > b:
            print("Takahashi")
        elif a < b:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
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
Suggestion 7

def main():
    A,B,C = map(int,input().split())

    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 8

def solve(A, B, C):
    if C == 0:
        if A > B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if B > A:
            return 'Aoki'
        else:
            return 'Takahashi'
