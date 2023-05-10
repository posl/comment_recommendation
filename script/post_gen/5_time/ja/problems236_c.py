Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if s[0] == t[0] and s[n-1] == t[m-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

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
Suggestion 3

def solve():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))

    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append("Yes")
        else:
            ans.append("No")
    for i in range(N):
        print(ans[i])
    return 0

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N, M)
    #print(S)
    #print(T)
    #print(S[0])
    #print(T[0])
    #print(S[N-1])
    #print(T[M-1])
    if S[0] == T[0] and S[N-1] == T[M-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    S_index = 0
    T_index = 0
    for i in range(N):
        if S[S_index] == T[T_index]:
            T_index += 1
            if T_index == M:
                print("Yes")
                return
        S_index += 1
    print("No")
main()

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    while i < N and j < M:
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
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[N-1] == T[M-1]:
        print("Yes")
    else:
        print("No")
