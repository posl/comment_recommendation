Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 2

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A, B)

=======
Suggestion 3

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    elif U == T:
        print(A, B-1)

=======
Suggestion 4

def solve():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 5

def main():
    # input
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    # compute
    if U == S:
        A -= 1
    else:
        B -= 1
    # output
    print(A, B)

=======
Suggestion 6

def main():
    s,t = input().split()
    a,b = input().split()
    u = input()
    if u == s:
        print(int(a)-1, b)
    else:
        print(a, int(b)-1)

=======
Suggestion 7

def main():
    S,T = input().rstrip().split()
    A,B = map(int,input().rstrip().split())
    U = input().rstrip()
    if S==U:
        A -= 1
    else:
        B -= 1
    print(A,B)

=======
Suggestion 8

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line1 = input()
    input_line2 = input()
    input_line3 = input()
    # スペースで分割して、input_line1,input_line2,input_line3に再代入
    S,T = input_line1.split()
    A,B = input_line2.split()
    U = input_line3
    # 出力
    if U == S:
        print(int(A)-1, int(B))
    else:
        print(int(A), int(B)-1)

=======
Suggestion 9

def main():
    # 標準入力から1行取得
    s, t = input().split()
    a, b = input().split()
    u = input()
    if u == s:
        print(int(a)-1, b)
    elif u == t:
        print(a, int(b)-1)
    else:
        print(a, b)
