Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    elif a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if cards[0] == cards[1] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a.count(a[0]) == 2 and a.count(a[4]) == 3:
        print("Yes")
    elif a.count(a[0]) == 3 and a.count(a[4]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int,input().split())
    if a==b and a==c and d==e:
        print("Yes")
    elif a==b and c==d and c==e:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print('No')
    elif a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    # 入力
    a = list(map(int, input().split()))
    a.sort()
    # 処理
    if a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print('No')
    elif a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    # データ入力
    a,b,c,d,e = map(int,input().split())
    # フルハウスの条件を満たすかどうか判定
    if ((a == b and b == c and d == e) or
        (a == b and c == d and d == e)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    if A==B and A==C and D==E:
        print('Yes')
    elif A==B and C==D and C==E:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    A,B,C,D,E = map(int,input().split())
    if A == B and C == D and D == E:
        print("No")
    elif A == B and B == C and D == E:
        print("Yes")
    elif A == B and B == C and C == D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print("No")
    elif a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("No")
    else:
        print("Yes")
