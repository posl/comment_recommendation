Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A,B)

=======
Suggestion 2

def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,b)

=======
Suggestion 3

def main():
    # 读入数据
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    # 处理并输出结果
    if s == u:
        a -= 1
    elif t == u:

=======
Suggestion 4

def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a,b)

=======
Suggestion 5

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        print(a-1, b)
    else:
        print(a, b-1)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    s, t = input().split()
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,

=======
Suggestion 7

def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    print(a,b)
