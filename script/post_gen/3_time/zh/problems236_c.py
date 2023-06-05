Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    print('Yes')
    for i in range(1,n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')
    print('Yes')

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")
