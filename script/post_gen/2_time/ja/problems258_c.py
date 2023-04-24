Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 2

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
Suggestion 3

def main():
    n,q = map(int,input().split())
    s = input()
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        x -= 1
        if t == 1:
            S = S[N-1] + S[:N-1]
        else:
            print(S[x])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()

    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N - x:] + S[:N - x]
        else:
            print(S[x - 1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = input().split()
        x = int(x)
        if t == "1":
            s = s[-x:]+s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = input().split()
        x = int(x)
        if t == '1':
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 8

def main():
    N,Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t,x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x-1])

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            x = x - 1
            s = s[-x:] + s[:-x]
            #print(s)
        elif t == 2:
            x = x - 1
            print(s[x])
        else:
            print("error")
