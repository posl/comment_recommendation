Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x)+1)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            return
