Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e = map(int, input().split())
    if (a == b == c and d == e) or (a == b and c == d == e):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A,B,C,D,E = map(int,input().split())
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and C == D and D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if (cards[0] == cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] == cards[4]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A,B,C,D,E = map(int,input().split())
    if A==B==C:
        if D==E:
            print("Yes")
        else:
            print("No")
    elif A==B:
        if C==D==E:
            print("Yes")
        else:
            print("No")
    elif A==C:
        if B==D==E:
            print("Yes")
        else:
            print("No")
    elif B==C:
        if A==D==E:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()

=======
Suggestion 5

def main():
    # 入力
    A, B, C, D, E = map(int, input().split())
    # 処理
    if A == B == C and D == E:
        print("Yes")
    elif A == B and C == D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    #入力
    a,b,c,d,e = map(int,input().split())
    #出力
    print("Yes" if (a==b==c and d==e) or (a==b and c==d==e) else "No")

=======
Suggestion 7

def main():
    a = input()
    b = list(map(int, a.split()))
    c = sorted(b)
    if c[0] == c[1] and c[1] == c[2] and c[3] == c[4]:
        print('Yes')
    elif c[0] == c[1] and c[2] == c[3] and c[3] == c[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #入力
    A,B,C,D,E = map(int,input().split())
    #フルハウスかどうかの判定
    if (A==B and B==C and D==E) or (A==B and C==D and D==E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #入力
    A,B,C,D,E = map(int,input().split())

    #フルハウスかどうかを判定
    if A == B and B == C and (D == E or D != E):
        print("Yes")
    elif A == B and B != C and (C == D and D == E):
        print("Yes")
    elif A != B and (B == C and C == D and D != E):
        print("Yes")
    elif A != B and (B != C and C == D and D == E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # 入力
    A,B,C,D,E = map(int, input().split())

    # 処理
    if (A == B) and (A == C) and (D == E):
        print("Yes")
    elif (A == B) and (C == D) and (C == E):
        print("Yes")
    else:
        print("No")
