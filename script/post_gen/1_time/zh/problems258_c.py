Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    n, q = map(int, input().split())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n-x:] + s[:n-x]
        else:
            print(s[x-1])

=======
Suggestion 2

def main():
    n,q = map(int,input().split())
    s = input()
    queries = []
    for _ in range(q):
        queries.append(input().split())

    #print(n,q,s,queries)

    #print(s[int(queries[0][1])-1])

    for i in range(q):
        if int(queries[i][0]) == 1:
            s = s[-1] + s[:-1]
        else:
            print(s[int(queries[i][1])-1])

=======
Suggestion 3

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
Suggestion 4

def problem258_c():
    n,q = map(int,input().split())
    s = input()
    for _ in range(q):
        t,x = map(int,input().split())
        if t==1:
            s = s[-x:]+s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]
    for t, x in query:
        if t == '1':
            S = S[-int(x):] + S[:-int(x)]
        else:
            print(S[int(x) - 1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x - 1])

=======
Suggestion 7

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
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = list(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x-1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x - 1])
