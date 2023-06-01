Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if (cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]) or (cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    # 读取输入
    a, b, c, d, e = map(int, input().split())

    # 处理
    if a == b and b == c:
        if d == e:
            print("Yes")
        else:
            print("No")
    elif a == b and b == d:
        if c == e:
            print("Yes")
        else:
            print("No")
    elif a == b and b == e:
        if c == d:
            print("Yes")
        else:
            print("No")
    elif a == c and c == d:
        if b == e:
            print("Yes")
        else:
            print("No")
    elif a == c and c == e:
        if b == d:
            print("Yes")
        else:
            print("No")
    elif a == d and d == e:
        if b == c:
            print("Yes")
        else:
            print("No")
    elif b == c and c == d:
        if a == e:
            print("Yes")
        else:
            print("No")
    elif b == c and c == e:
        if a == d:
            print("Yes")
        else:
            print("No")
    elif b == d and d == e:
        if a == c:
            print("Yes")
        else:
            print("No")
    elif c == d and d == e:
        if a == b:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[2] == a[4] or a[0] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a = input()
    b = a.split()
    b.sort()
    if b[0] == b[1] and b[1] != b[2] and b[2] == b[3] and b[3] == b[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # output
    if (A == B and B == C) or (A == B and B == D) or (A == B and B == E) or (A == C and C == D) or (A == C and C == E) or (A == D and D == E) or (B == C and C == D) or (B == C and C == E) or (B == D and D == E) or (C == D and D == E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a = input().split()
    if a.count(a[0]) == 3 or a.count(a[1]) == 3 or a.count(a[2]) == 3 or a.count(a[3]) == 3 or a.count(a[4]) == 3:
        if a.count(a[0]) == 2 or a.count(a[1]) == 2 or a.count(a[2]) == 2 or a.count(a[3]) == 2 or a.count(a[4]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 读入数据
    A, B, C, D, E = map(int, input().split())
    # 判断是否为满堂红
    if A == B == C or A == B == D or A == B == E or A == C == D or A == C == E or A == D == E or B == C == D or B == C == E or B == D == E or C == D == E:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def judge():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

judge()
