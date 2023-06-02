Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # 处理数据
    if u == s:
        a -= 1
    else:
        b -= 1

    # 输出结果
    print(a, b)

=======
Suggestion 2

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        print(a-1, b)
    elif t == u:
        print(a, b-1)

=======
Suggestion 3

def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    print(a,b)

=======
Suggestion 4

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 5

def get_input():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    return s, t, a, b, u

=======
Suggestion 6

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        print(a - 1, b)
    else:
        print(a, b - 1)
