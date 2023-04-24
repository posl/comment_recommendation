Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[4]:
        print('Yes')
    elif a[0] == a[2] and a[3] == a[4]:
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
    a,b,c,d,e = map(int, input().split())
    if a==b==c and d==e:
        print("Yes")
    elif a==b and c==d==e:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    if (A==B and B==C and D==E) or (A==B and C==D and D==E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    cards = input().split()
    cards.sort()
    if (cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

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
Suggestion 7

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    if (A == B and C == D and B != C) or (A == C and B == D and C != B) or (A == D and B == E and D != B) or (A == E and B == C and A != B) or (A == B and C == E and A != C):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # data load
    data = input().rstrip().split(" ")
    # data[0] = A
    # data[1] = B
    # data[2] = C
    # data[3] = D
    # data[4] = E

    # フルハウスの条件を満たすかどうかを判定する
    if data.count(data[0]) == 3 and data.count(data[1]) == 2:
        print("Yes")
    elif data.count(data[0]) == 2 and data.count(data[1]) == 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #input
    a,b,c,d,e = map(int, input().split())

    #compute
    if(a==b==c and d==e):
        print('Yes')
    elif(a==b and c==d==e):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    # データ入力
    a,b,c,d,e = map(int,input().split())
    # データ処理
    if a == b and b == c and d == e:
        print("Yes")
    elif a == b and c == d and d == e:
        print("Yes")
    else:
        print("No")
    # 出力
