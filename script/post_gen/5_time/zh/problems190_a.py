Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 输入
    a, b, c = map(int, input().split())

    # 处理
    if c == 0:
        # 高桥先做
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        # 青木先做
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
Suggestion 4

def problem190_a():
    a,b,c = map(int, input().split())
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

main()

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
        if a >= b:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 7

def whoWin(A,B,C):
    if C==0:
        if A>B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if A>=B:
            return 'Takahashi'
        else:
            return 'Aoki'

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if a > b:
        print("Takahashi")
    elif a < b:
        print("Aoki")
    else:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")
main()

=======
Suggestion 9

def main():
    a,b,c=map(int,input().split())
    if c==0:
        if a>b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a>=b:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 10

def game(a,b,c):
    if c == 0:
        if a > b:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if a >= b:
            return 'Takahashi'
        else:
            return 'Aoki'
