Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = list(map(str, input().split()))
    T = list(map(str, input().split()))
    for i in range(0, N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')
