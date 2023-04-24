Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
    elif abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
    elif abs(r1 + c1 - r2 - c2) <= 3:
        print(2)
    elif abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 4

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    d1 = abs(r1 - c1)
    d2 = abs(r2 - c2)
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        print(1)
        return
    if d1 == d2 or d1 % 2 == d2 % 2:
        print(2)
        return
    print(3)

=======
Suggestion 5

def main():

    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return

    print(3)

=======
Suggestion 6

def main():
    # 入力
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    # 出力
    print(solve(r1, c1, r2, c2))

=======
Suggestion 7

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    #r1, c1, r2, c2 = 1, 1, 5, 6
    #r1, c1, r2, c2 = 1, 1, 1, 200001
    #r1, c1, r2, c2 = 2, 3, 998244353, 998244853
    #r1, c1, r2, c2 = 1, 1, 1, 1

    #print(r1, c1, r2, c2)
    #print(abs(r1 - r2), abs(c1 - c2))
    #print(abs(r1 - r2) + abs(c1 - c2))
    #print(abs(r1 - r2) + abs(c1 - c2) - 1)
    #print(abs(r1 - r2) + abs(c1 - c2) - 2)
    #print(abs(r1 - r2) + abs(c1 - c2) - 3)
    #print(abs(r1 - r2) + abs(c1 - c2) - 4)

    #print((r1 + c1) - (r2 + c2))
    #print((r1 - c1) - (r2 - c2))
    #print(abs((r1 + c1) - (r2 + c2)))
    #print(abs((r1 - c1) - (r2 - c2)))

    if r1 == r2 and c1 == c2:
        print(0)
    elif (r1 + c1) == (r2 + c2) or (r1 - c1) == (r2 - c2) or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) -

=======
Suggestion 8

def calc(r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return 0
    if r1+c1==r2+c2:
        return 1
    if r1-c1==r2-c2:
        return 1
    if abs(r1-r2)+abs(c1-c2)<=3:
        return 1
    if (r1+c1)%2==(r2+c2)%2:
        return 2
    if abs(r1-r2)+abs(c1-c2)<=6:
        return 2
    if abs((r1+c1)//2-(r2+c2)//2)+abs((r1-c1)//2-(r2-c2)//2)<=3:
        return 2
    return 3

r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
print(calc(r1,c1,r2,c2))

=======
Suggestion 9

def main():
    r1, c1 = map(int, input().split()) # r1, c1
    r2, c2 = map(int, input().split()) # r2, c2
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
    else:
        print(3)
