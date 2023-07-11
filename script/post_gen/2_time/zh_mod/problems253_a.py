Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入a, b, c
    a, b, c = map(int, input().split())

    # 判断b是否是中位数
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a <= 100 and b <= 100 and c <= 100:
        if a <= b <= c or c <= b <= a:

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if (a <= b and b <= c) or (c <= b and b <= a):
        print("Yes")
    el

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if (a <= b <= c) or (c <= b <= a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if(a <= b and b <= c) or (c <= b and b <= a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def findMedian(a,b,c):
    if a>b:
        if b>c:
            return b
        elif a>c:
            return c
        else:
            return a
    else:
