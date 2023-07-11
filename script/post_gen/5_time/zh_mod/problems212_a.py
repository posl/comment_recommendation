Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def alloy(a,b):
    if a == 0:
        return 'Silver'
    elif b == 0:
        return 'Gold'
    else:
        return 'Alloy'

=======
Suggestion 2

def problem212_a():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b >

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a == 0 and b != 0:
        print('Silver')
    elif a != 0 and b == 0:

=======
Suggestion 5

def problem212_a():
    a,b = map(int, input().split())
    if a == 0:
        print("Silver")
    elif b == 0:
        print("

=======
Suggestion 6

def main():
    # 读取输入
    gold, silver = map(int, input().split())
    # 判断
    if gold == 0:
        if silver == 0:

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if A>0 and B==0:
        print("Gold")
    elif A==0 and B>0:
        print(

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    if A == 0:
        print("Silver")
    elif B == 0:
        print("Gold")
