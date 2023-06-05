Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i + 1)
            break

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 3

def get_input():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    return n, x, p

=======
Suggestion 4

def solution():
    n,x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    print p.index(x)+1

=======
Suggestion 5

def solve(n, x, p):
    for i in range(n):
        if p[i] == x:
            return i+1

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

=======
Suggestion 7

def main():
    n,x = input().split(" ")
    n = int(n)
    x = int(x)
    p = input().split(" ")
    for i in range(n):
        p[i] = int(p[i])
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break
