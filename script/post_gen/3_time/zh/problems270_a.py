Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(7-a+7-b)

=======
Suggestion 2

def solve():
    a,b = map(int,input().split())
    print(7-a+7-b)
solve()

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    print(7-A+7-B)

=======
Suggestion 4

def get_snuke_score(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 2
    elif a == 0 and b == 2:
        return 1
    elif a == 0 and b == 3:
        return 3
    elif a == 0 and b == 4:
        return 1
    elif a == 0 and b == 5:
        return 2
    elif a == 0 and b == 6:
        return 1
    elif a == 0 and b == 7:
        return 0
    elif a == 1 and b == 0:
        return 2
    elif a == 1 and b == 1:
        return 3
    elif a == 1 and b == 2:
        return 2
    elif a == 1 and b == 3:
        return 4
    elif a == 1 and b == 4:
        return 2
    elif a == 1 and b == 5:
        return 3
    elif a == 1 and b == 6:
        return 2
    elif a == 1 and b == 7:
        return 1
    elif a == 2 and b == 0:
        return 1
    elif a == 2 and b == 1:
        return 2
    elif a == 2 and b == 2:
        return 1
    elif a == 2 and b == 3:
        return 3
    elif a == 2 and b == 4:
        return 1
    elif a == 2 and b == 5:
        return 2
    elif a == 2 and b == 6:
        return 1
    elif a == 2 and b == 7:
        return 0
    elif a == 3 and b == 0:
        return 3
    elif a == 3 and b == 1:
        return 4
    elif a == 3 and b == 2:
        return 3
    elif a == 3 and b == 3:
        return 5
    elif a == 3 and b == 4:
        return

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(7-a+7-b)
main()

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(a ^ b)

=======
Suggestion 7

def getScore(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b + 1
    elif b == 0:
        return a + 1
    else:
        return a + b + 1

=======
Suggestion 8

def main():
    A,B = map(int, input().split())
    if A >= 4:
        A -= 4
    if B >= 4:
        B -= 4
    print(7 - A - B)
