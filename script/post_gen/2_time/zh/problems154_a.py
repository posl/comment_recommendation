Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #读取输入
    S,T = input().split()
    A,B = input().split()
    U = input()

    #处理输入
    if S == U:
        A = str(int(A) - 1)
    else:
        B = str(int(B) - 1)

    #输出结果
    print(A,B)

=======
Suggestion 2

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,b)

=======
Suggestion 3

def main():
    S, T = input().split()
    A, B = input().split()
    U = input()
    if S == U:
        print(int(A)-1, B)
    else:
        print(A, int(B)-1)

=======
Suggestion 4

def main():
    S,T = input().split()
    A,B = map(int,input().split())
    U = input()

    if U == S:
        A -= 1
    elif U == T:
        B -= 1

    print(A,B)

=======
Suggestion 5

def main():
    s,t = input().split()
    a,b = input().split()
    u = input()
    a = int(a)
    b = int(b)
    if s == u:
        a = a - 1
    else:
        b = b - 1
    print(a,b)

=======
Suggestion 6

def main():
    #输入
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    #处理
    if s == u:
        a -= 1
    elif t == u:
        b -= 1
    #输出
    print(a,b)

=======
Suggestion 7

def main():
    S, T = input().split(' ')
    A, B = map(int, input().split(' '))
    U = input()
    if S == U:
        A -= 1
    else:
        B -= 1
    print(A, B)

=======
Suggestion 8

def main():
    # 读入S和T
    s, t = input().split()
    # 读入A和B
    a, b = map(int, input().split())
    # 读入U
    u = input()
    # 计算答案并打印
    if u == s:
        print(a - 1, b)
    elif u == t:
        print(a, b - 1)
