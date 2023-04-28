Synthesizing 10/10 solutions

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
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[N-1] == T[M-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = list(map(str,input().split()))
    t = list(map(str,input().split()))
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
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
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    i = 0
    j = 0
    while i < n:
        if s[i] == t[j]:
            j += 1
            if j == m:
                break
        i += 1
    if j == m:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()

    i = 0
    j = 0
    while i < N:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()

    s = 0
    for i in range(N):
        if S[i] == T[s]:
            s += 1
            if s == M:
                break
    for i in range(N):
        if S[i] == T[s]:
            print("Yes")
            s += 1
            if s == M:
                break
        else:
            print("No")

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    s_list = input().split()
    t_list = input().split()

    s_dict = {}
    t_dict = {}
    for i in range(n):
        s_dict[s_list[i]] = i
    for i in range(m):
        t_dict[t_list[i]] = i

    for i in range(n):
        if s_dict[s_list[i]] == t_dict[s_list[i]]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    print("Yes" if t[0] in s and t[-1] in s and s.index(t[0]) < s.index(t[-1]) else "No")
