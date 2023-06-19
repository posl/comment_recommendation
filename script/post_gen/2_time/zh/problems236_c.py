Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")
solve()

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
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())

    if n < m:
        print("No")
        return

    for i in range(n):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def solve():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = i
    t_dict = {}
    for i in range(m):
        t_dict[t[i]] = i
    for i in range(n):
        if s[i] in t_dict:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

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
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def solve():
    n,m = map(int,input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")
