Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    if U == S:
        A -= 1
    else:
        B -= 1

    print(A, B)

=======
Suggestion 2

def main():
    S,T = input().split()
    A,B = input().split()
    U = input()
    if S == U:
        A = int(A) - 1
    elif T == U:
        B = int(B) - 1
    print(A,B)

=======
Suggestion 3

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 4

def main():
    s,t = input().split()
    a,b = input().split()
    u = input()
    if s == u:
        print(int(a)-1,b)
    else:
        print(a,int(b)-1)

=======
Suggestion 5

def main():
    # 读取输入
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    # 处理
    if u == s:
        a -= 1
    elif u == t:
        b -= 1

    # 输出结果
    print(a, b)

=======
Suggestion 6

def main():
    S, T = map(str, input().split())
    A, B = map(int, input().split())
    U = str(input())

    if S == U:
        A -= 1
    else:
        B -= 1

    print(A, B)

=======
Suggestion 7

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    print(a,b)

=======
Suggestion 8

def main():
    S,T = map(str, input().split())
    A,B = map(int, input().split())
    U = str(input())
    if U == S:
        A = A - 1
    elif U == T:
        B = B - 1
    print(A,B)

=======
Suggestion 9

def main():
    s = input().split()
    a,b = map(int, input().split())
    u = input()
    
    if s[0] == u:
        a -= 1
    else:
        b -= 1
    
    print(a,b)
