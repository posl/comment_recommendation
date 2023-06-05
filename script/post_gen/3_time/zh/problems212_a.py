Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print("error")
    elif a == 0:
        print("silver")
    elif b == 0:
        print("gold")
    else:
        print("alloy")

=======
Suggestion 3

def main():
    a,b=map(int,input().split())
    if a>0 and b>0:
        print('合金')
    elif a>0 and b==0:
        print('黄金')
    elif a==0 and b>0:
        print('银')

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if 0<A and B==0:
        print("黄金")
    elif A==0 and 0<B:
        print("银")
    else:
        print("合金")

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A == 0:
        print('银')
    elif B == 0:
        print('黄金')
    else:
        print('合金')

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a>0 and b>0:
        print("合金")
    elif a>0 and b==0:
        print("黄金")
    elif a==0 and b>0:
        print("银")

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A == 0:
        print("银")
    elif B == 0:
        print("黄金")
    else:
        print("合金")

=======
Suggestion 8

def judge(a,b):
    if a>0 and b==0:
        print('黄金')
    elif a==0 and b>0:
        print('银')
    else:
        print('合金')

judge(100,2)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a>0 and b==0:
        print("黄金")
    elif a==0 and b>0:
        print("银")
    elif a>0 and b>0:
        print("合金")
