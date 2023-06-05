Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    #print(A,B)
    if A == 0 and B == 0:
        print(0)
    elif A == 0 and B == 1:
        print(2)
    elif A == 0 and B == 2:
        print(1)
    elif A == 0 and B == 3:
        print(3)
    elif A == 0 and B == 4:
        print(1)
    elif A == 0 and B == 5:
        print(2)
    elif A == 0 and B == 6:
        print(1)
    elif A == 0 and B == 7:
        print(4)
    elif A == 1 and B == 0:
        print(2)
    elif A == 1 and B == 1:
        print(0)
    elif A == 1 and B == 2:
        print(3)
    elif A == 1 and B == 3:
        print(1)
    elif A == 1 and B == 4:
        print(4)
    elif A == 1 and B == 5:
        print(2)
    elif A == 1 and B == 6:
        print(3)
    elif A == 1 and B == 7:
        print(1)
    elif A == 2 and B == 0:
        print(1)
    elif A == 2 and B == 1:
        print(3)
    elif A == 2 and B == 2:
        print(0)
    elif A == 2 and B == 3:
        print(4)
    elif A == 2 and B == 4:
        print(1)
    elif A == 2 and B == 5:
        print(3)
    elif A == 2 and B == 6:
        print(2)
    elif A == 2 and B == 7:
        print(4)
    elif A == 3 and B == 0:
        print(3)
    elif A == 3 and B == 1:
        print(1)
    elif A == 3 and B == 2:
        print(4)
    elif A == 3 and B == 3:
        print(0)
    elif A == 3

=======
Suggestion 2

def problems270_a():
    a,b = map(int,input().split())
    if a==0 and b==0:
        print(0)
    elif a==0 or b==0:
        print(4)
    elif a==1 and b==1:
        print(2)
    elif a==1 or b==1:
        print(3)
    elif a==2 and b==2:
        print(0)
    elif a==2 or b==2:
        print(1)
    elif a==3 and b==3:
        print(4)
    elif a==3 or b==3:
        print(5)
    elif a==4 and b==4:
        print(0)
    elif a==4 or b==4:
        print(1)
    elif a==5 and b==5:
        print(2)
    elif a==5 or b==5:
        print(3)
    elif a==6 and b==6:
        print(4)
    elif a==6 or b==6:
        print(5)
    elif a==7 and b==7:
        print(0)
    elif a==7 or b==7:
        print(1)
    else:
        print('error')
    return 0

problems270_a()

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        print(0)
    elif A == 0 and B == 1:
        print(2)
    elif A == 0 and B == 2:
        print(4)
    elif A == 0 and B == 3:
        print(6)
    elif A == 0 and B == 4:
        print(8)
    elif A == 0 and B == 5:
        print(10)
    elif A == 0 and B == 6:
        print(12)
    elif A == 0 and B == 7:
        print(14)
    elif A == 1 and B == 0:
        print(1)
    elif A == 1 and B == 1:
        print(3)
    elif A == 1 and B == 2:
        print(5)
    elif A == 1 and B == 3:
        print(7)
    elif A == 1 and B == 4:
        print(9)
    elif A == 1 and B == 5:
        print(11)
    elif A == 1 and B == 6:
        print(13)
    elif A == 1 and B == 7:
        print(15)
    elif A == 2 and B == 0:
        print(2)
    elif A == 2 and B == 1:
        print(4)
    elif A == 2 and B == 2:
        print(6)
    elif A == 2 and B == 3:
        print(8)
    elif A == 2 and B == 4:
        print(10)
    elif A == 2 and B == 5:
        print(12)
    elif A == 2 and B == 6:
        print(14)
    elif A == 2 and B == 7:
        print(16)
    elif A == 3 and B == 0:
        print(3)
    elif A == 3 and B == 1:
        print(5)
    elif A == 3 and B == 2:
        print(7)
    elif A == 3 and B == 3:
        print(9)
    elif A == 3 and B == 4:

=======
Suggestion 4

def getScore(a,b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 0 and b == 2:
        return 2
    if a == 0 and b == 3:
        return 3
    if a == 0 and b == 4:
        return 4
    if a == 0 and b == 5:
        return 5
    if a == 0 and b == 6:
        return 6
    if a == 0 and b == 7:
        return 7
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 2
    if a == 1 and b == 2:
        return 3
    if a == 1 and b == 3:
        return 4
    if a == 1 and b == 4:
        return 5
    if a == 1 and b == 5:
        return 6
    if a == 1 and b == 6:
        return 7
    if a == 1 and b == 7:
        return 8
    if a == 2 and b == 0:
        return 2
    if a == 2 and b == 1:
        return 3
    if a == 2 and b == 2:
        return 4
    if a == 2 and b == 3:
        return 5
    if a == 2 and b == 4:
        return 6
    if a == 2 and b == 5:
        return 7
    if a == 2 and b == 6:
        return 8
    if a == 2 and b == 7:
        return 9
    if a == 3 and b == 0:
        return 3
    if a == 3 and b == 1:
        return 4
    if a == 3 and b == 2:
        return 5
    if a == 3 and b == 3:
        return 6
    if a == 3 and b == 4:
        return 7
    if

=======
Suggestion 5

def solve():
    A,B = map(int,input().split())
    C = 0
    if A == 0 and B == 0:
        C = 0
    elif A == 0 and B == 1:
        C = 2
    elif A == 0 and B == 2:
        C = 4
    elif A == 0 and B == 3:
        C = 6
    elif A == 0 and B == 4:
        C = 8
    elif A == 0 and B == 5:
        C = 10
    elif A == 0 and B == 6:
        C = 12
    elif A == 0 and B == 7:
        C = 14
    elif A == 1 and B == 0:
        C = 1
    elif A == 1 and B == 1:
        C = 3
    elif A == 1 and B == 2:
        C = 5
    elif A == 1 and B == 3:
        C = 7
    elif A == 1 and B == 4:
        C = 9
    elif A == 1 and B == 5:
        C = 11
    elif A == 1 and B == 6:
        C = 13
    elif A == 1 and B == 7:
        C = 15
    elif A == 2 and B == 0:
        C = 2
    elif A == 2 and B == 1:
        C = 3
    elif A == 2 and B == 2:
        C = 6
    elif A == 2 and B == 3:
        C = 7
    elif A == 2 and B == 4:
        C = 10
    elif A == 2 and B == 5:
        C = 11
    elif A == 2 and B == 6:
        C = 14
    elif A == 2 and B == 7:
        C = 15
    elif A == 3 and B == 0:
        C = 4
    elif A == 3 and B == 1:
        C = 5
    elif A == 3 and B == 2:
        C

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print(7 - A - B)

=======
Suggestion 7

def solve(a, b):
    if a == b:
        return a
    else:
        return 7 - a - b

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    print(7-a+7-b)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print(0)
    elif a == 0 and b != 0:
        print(b)
    elif a != 0 and b == 0:
        print(a)
    else:
        print(7-a-b)

=======
Suggestion 10

def solve():
    a,b = map(int,input().split())
    print(7-a+7-b)
