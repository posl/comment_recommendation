Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    print(32**(A-B))

=======
Suggestion 2

def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    if A < 3 or A > 9 or B < 3 or B > 9:
        print("输入错误")
    else:
        print(32 ** (A - B))

=======
Suggestion 3

def problems221_a():
    a,b = map(int,input().split())
    print(32**(a-b))

=======
Suggestion 4

def main():
    #print("请输入两个整数，中间用空格隔开")
    a,b = map(int,input().split())
    #print("a=",a,"b=",b)
    print(32**(a-b))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    print(32**(a-b))
