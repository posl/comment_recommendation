Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def findX(P, X):
    for i in range(len(P)):
        if P[i] == X:
            return i+1

=======
Suggestion 2

def main():
    n,x=map(int,input().split())
    p=list(map(int,input().split()))
    print(p.index(x)+1)

=======
Suggestion 3

def get_input():
    n,x = map(int,input().split())
    p = list(map(int,input().split()))
    return n,x,p

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

=======
Suggestion 5

def get_input():
    input1 = input("请输入两个数，以空格分开：")
    input2 = input("请输入一个数，以空格分开：")
    input1 = input1.split(" ")
    input2 = input2.split(" ")
    # print(input1)
    # print(input2)
    return input1, input2

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)

=======
Suggestion 7

def solve():
    #获取输入
    n = int(input().strip())
    x = int(input().strip())
    p = list(map(int, input().strip().split()))
    #处理
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break
