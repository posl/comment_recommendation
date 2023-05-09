Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 2

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
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[0:N-x]
        else:
            print(S[x-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 2:
            print(S[x-1])
        else:
            S = S[-x:] + S[:-x]

=======
Suggestion 6

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
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x - 1])

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    S = input()
    query = []
    for _ in range(Q):
        query.append(list(map(str,input().split())))
    for q in query:
        if q[0] == '1':
            S = S[-int(q[1]):] + S[:-int(q[1])]
        else:
            print(S[int(q[1])-1])
