Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

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
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
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
    s = list(s)
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s.insert(0, s.pop())
        else:
            print(s[x - 1])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    s = input()
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            s = s[-x:]+s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    s = input()
    #print(n, q)
    #print(s)
    for i in range(q):
        t, x = map(int, input().split())
        #print(t, x)
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    query = [input().split() for _ in range(q)]
    s = list(s)
    for i in range(q):
        if query[i][0] == "1":
            s[int(query[i][1])-1], s[int(query[i][1])] = s[int(query[i][1])], s[int(query[i][1])-1]
        else:
            print(s[int(query[i][1])-1])
