Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,b = map(int,input().split())
    print(n-a+b)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(n + b - a)

=======
Suggestion 3

def main():
    N,A,B = map(int, input().split())
    print(N-A+B)

=======
Suggestion 4

def main():
    print("请输入N A B:")
    str = input()
    str_list = str.split(" ")
    N = int(str_list[0])
    A = int(str_list[1])
    B = int(str_list[2])
    print(N + B - A)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print(N + B - A)

main()

=======
Suggestion 6

def main():
    n,a,b = map(int,input().split())
    print(n+a-b)

=======
Suggestion 7

def main():
    #print("请输入三个整数，用空格隔开：")
    #num = input()
    #num = num.split()
    #N = int(num[0])
    #A = int(num[1])
    #B = int(num[2])
    N = 100
    A = 2
    B = 1
    print(N-A+B)

=======
Suggestion 8

def main():
    print("请输入N A B:")
    N,A,B = map(int,input().split())
    if 100<=N<=200 and 1<=A<=100 and 1<=B<=100:
        print(N+A-B)
    else:
        print("输入的数值不符合条件！")
