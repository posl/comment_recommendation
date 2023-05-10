Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    if U == S:
        print(str(A-1) + " " + str(B))
    else:
        print(str(A) + " " + str(B-1))

=======
Suggestion 2

def main():
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 3

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 4

def main():
    # 文字列S,Tと整数A,Bと文字列Uの入力を取得
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    # 文字列S,TがそれぞれUと同じかどうかで条件分岐
    if S == U:
        A -= 1
    else:
        B -= 1
    # 結果を出力
    print(A,B)

=======
Suggestion 5

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
Suggestion 6

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()

    if s == u:
        a -= 1
    else:
        b -= 1

    print(a,b)

=======
Suggestion 7

def solve():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)
