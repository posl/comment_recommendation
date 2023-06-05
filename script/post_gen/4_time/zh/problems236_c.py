Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

main()

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    d = {}
    for s in S:
        d[s] = 'No'
    for t in T:
        d[t] = 'Yes'
    for s in S:
        print(d[s])

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

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

def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    for s in S:
        if s in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = list(input().split())
    t = list(input().split())
    for i in s:
        if i in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    S = input().split()
    T = input().split()
    for i in range(n):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")
