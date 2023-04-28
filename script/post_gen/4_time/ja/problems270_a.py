Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c = a + b
    if c == 0:
        print(0)
    elif c == 1:
        print(2)
    elif c == 2:
        print(1)
    elif c == 3:
        print(0)
    elif c == 4:
        print(4)
    elif c == 5:
        print(3)
    elif c == 6:
        print(2)
    elif c == 7:
        print(1)
    elif c == 8:
        print(0)

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    c = 0
    if a == 0 and b == 0:
        print(0)
    elif a == 0 or b == 0:
        print(1)
    else:
        print(2)

=======
Suggestion 3

def main():
    a = input()
    a = a.split()
    A = int(a[0])
    B = int(a[1])
    if A == 0 and B == 0:
        print(0)
    elif A == 1 and B == 0:
        print(1)
    elif A == 0 and B == 1:
        print(1)
    elif A == 2 and B == 0:
        print(2)
    elif A == 0 and B == 2:
        print(2)
    elif A == 1 and B == 1:
        print(2)
    elif A == 4 and B == 0:
        print(4)
    elif A == 0 and B == 4:
        print(4)
    elif A == 3 and B == 0:
        print(3)
    elif A == 0 and B == 3:
        print(3)
    elif A == 2 and B == 1:
        print(3)
    elif A == 1 and B == 2:
        print(3)
    elif A == 2 and B == 2:
        print(4)
    elif A == 4 and B == 1:
        print(5)
    elif A == 1 and B == 4:
        print(5)
    elif A == 3 and B == 1:
        print(4)
    elif A == 1 and B == 3:
        print(4)
    elif A == 2 and B == 3:
        print(5)
    elif A == 3 and B == 2:
        print(5)
    elif A == 4 and B == 2:
        print(6)
    elif A == 2 and B == 4:
        print(6)
    elif A == 3 and B == 3:
        print(6)
    elif A == 4 and B == 3:
        print(7)
    elif A == 3 and B == 4:
        print(7)
    elif A == 4 and B == 4:
        print(8)

=======
Suggestion 4

def main():
    # input
    A, B = map(int, input().split())

    # compute
    S = A + B
    if S >= 15 and B >= 8:
        result = 1
    elif S >= 10 and B >= 3:
        result = 2
    elif S >= 3:
        result = 3
    else:
        result = 4

    # output
    print(result)

=======
Suggestion 5

def main():
    # 入力
    A, B = map(int, input().split())

    # 処理
    ans = 0
    if A == 0 and B == 0:
        ans = 0
    elif A == 0:
        ans = B - 1
    elif B == 0:
        ans = A - 1
    else:
        ans = A + B

    # 出力
    print(ans)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(7 - a - b)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    c = a^b
    print(c)

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    print(7-A-B)

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    print(3-a-b)
