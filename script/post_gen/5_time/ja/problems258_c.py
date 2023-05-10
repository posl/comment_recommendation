Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    s = input()
    queries = [list(map(str, input().split())) for _ in range(q)]
    for query in queries:
        if query[0] == '1':
            s = s[-int(query[1]):] + s[:-int(query[1])]
        else:
            print(s[int(query[1]) - 1])

=======
Suggestion 2

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
Suggestion 3

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
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n-x:] + s[:n-x]
        else:
            print(s[x-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(str, input().split())) for i in range(Q)]

    for i in range(Q):
        if query[i][0] == "1":
            S = S[-int(query[i][1]):] + S[:-int(query[i][1])]
        else:
            print(S[int(query[i][1])-1])

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    S = input()
    query = [list(map(str,input().split())) for _ in range(Q)]
    for i in range(Q):
        if query[i][0] == '1':
            S = S[-int(query[i][1]):] + S[:-int(query[i][1])]
        else:
            print(S[int(query[i][1])-1])

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    S = input()
    queries = [list(map(str,input().split())) for _ in range(Q)]
    for query in queries:
        if query[0] == '1':
            S = S[N-int(query[1]):] + S[:N-int(query[1])]
        else:
            print(S[int(query[1])-1])
