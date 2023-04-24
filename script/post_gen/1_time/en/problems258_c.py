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
            print(s[x - 1])

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
            S = S[N-x:] + S[:N-x]
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

main()

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

main()

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    s = input()

    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[n - x:] + s[:n - x]
        else:
            print(s[x - 1])

=======
Suggestion 7

def processQueries(N, Q, S, queries):
    for query in queries:
        if query[0] == 1:
            S = S[-query[1]:] + S[:-query[1]]
        else:
            print(S[query[1]-1])

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    S = input()
    queries = []
    for i in range(Q):
        queries.append(list(input().split()))

    for i in range(Q):
        if queries[i][0] == '1':
            S = S[N-int(queries[i][1]):] + S[:N-int(queries[i][1])]
        else:
            print(S[int(queries[i][1])-1])

=======
Suggestion 9

def main():
    # input
    n, q = map(int, input().split())
    s = list(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # compute
    for t, x in queries:
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])
