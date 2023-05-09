Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')
    return

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if len(set(S) & set(T)) == M:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if all(s in T for s in S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] == T[i]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    #N, M = map(int, input().split())
    #S = input().split()
    #T = input().split()
    N, M = 5, 3
    S = "tokyo kanda akiba okachi ueno".split()
    T = "tokyo akiba ueno".split()

    for s in S:
        if s in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if len(s) == len(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if m > n:
        print("No")
        return
    for i in range(n):
        if s[i] == t[0]:
            break
    else:
        print("No")
        return
    for j in range(m):
        if s[j+i] != t[j]:
            print("No")
            return
    print("Yes")
