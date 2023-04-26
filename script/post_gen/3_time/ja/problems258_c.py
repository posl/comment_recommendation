Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    s = list(input())
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s.insert(0, s.pop(x - 1))
        else:
            print(s[x - 1])

=======
Suggestion 2

def main():
    n,q = map(int,input().split())
    s = input()
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            s = s[n-x:]+s[:n-x]
        else:
            print(s[x-1])

=======
Suggestion 3

def main():
    N,Q = map(int,input().split())
    S = input()
    S = S[::-1]
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            S = S[x:] + S[:x]
        else:
            print(S[x-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    T = []
    for i in range(Q):
        t, x = map(int, input().split())
        T.append([t, x])
    S = S[::-1]
    for i in range(Q):
        if T[i][0] == 1:
            S = S[:T[i][1]] + S[T[i][1]+1:] + S[T[i][1]]
        else:
            print(S[T[i][1]-1])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    s = input()
    s = list(s)
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            for j in range(x):
                s.insert(0,s.pop())
        else:
            print(s[x-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]

    for q in query:
        if q[0] == '1':
            S = S[-int(q[1]):] + S[:-int(q[1])]
        else:
            print(S[int(q[1])-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]
    for q in query:
        if q[0] == "1":
            S = S[-int(q[1]):] + S[0:N-int(q[1])]
        else:
            print(S[int(q[1])-1])

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    S = input()
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[N-int(query[1]):N] + S[0:N-int(query[1])]
        else:
            print(S[int(query[1])-1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    S = list(S)
    #print(S)
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S.insert(0, S.pop(x-1))
            #print(S)
        else:
            print(S[x-1])
            #print(S)

=======
Suggestion 10

def main():
    N,Q = map(int,input().split())
    S = input()
    #print(N,Q,S)
    S = list(S)
    #print(S)
    for i in range(Q):
        query = input().split()
        #print(query)
        if query[0] == '1':
            for j in range(int(query[1])):
                S.insert(0,S.pop())
        else:
            print(S[int(query[1])-1])
