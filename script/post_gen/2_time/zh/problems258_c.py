Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 2

def main():
    # 读入数据
    n, q = map(int, input().split())
    s = list(input())
    # 处理查询
    for i in range(q):
        t, x = input().split()
        if t == "1":
            s = s[-int(x):] + s[:-int(x)]
        else:
            print(s[int(x) - 1])

=======
Suggestion 3

def problem258_c():
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        t,x=map(int,input().split())
        if t==1:
            s=s[-x:]+s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 2:
            print(s[x-1])
        else:
            s = s[n-x:] + s[:n-x]

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    s = input()
    # print(n, q, s)
    for i in range(q):
        t, x = map(int, input().split())
        # print(t, x)
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    s = input()
    query = []
    for i in range(q):
        query.append(list(map(str, input().split())))
    for i in range(q):
        if query[i][0] == '1':
            s = s[-int(query[i][1]):] + s[:-int(query[i][1])]
        else:
            print(s[int(query[i][1])-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x - 1])

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t, x = map(str, input().split())
        x = int(x)
        if t == '1':
            s = s[-x:] + s[:-x]
        if t == '2':
            print(s[x - 1])

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n-x:] + s[:n-x]
        else:
            print(s[x-1])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[-1] + S[:-1]
        else:
            print(S[int(query[1])-1])
