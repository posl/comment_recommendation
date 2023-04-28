Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
                break
    print(count)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    count = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:] == T[j]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    count = 0
    for s in S:
        for t in T:
            if s.endswith(t):
                count += 1
                break
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    T = []
    for i in range(M):
        T.append(input())
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:6] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    print(sum(1 for s in S if s[-3:] in T))

=======
Suggestion 9

def main():
    # input
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # compute
    S.sort()
    T.sort()
    ans = 0
    i = 0
    j = 0
    while i < N and j < M:
        if S[i] == T[j]:
            ans += 1
            i += 1
            j += 1
        elif S[i] < T[j]:
            i += 1
        else:
            j += 1
    # output
    print(ans)

=======
Suggestion 10

def main():
    #print("Hello World!")
    N,M = input().split()
    N = int(N)
    M = int(M)
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    #print(N,M,S,T)
    #print(type(N),type(M),type(S),type(T))
    #print(N,M,S,T)
    #print(type(N),type(M),type(S),type(T))
    #print(S[0])
    #print(T[0])
    #print(S[0][3:6])
    #print(T[0][0:3])
    #print(S[0][3:6]==T[0][0:3])
    #print(S[0][3:6]==T[1][0:3])
    #print(S[0][3:6]==T[2][0:3])
    #print(S[0][3:6]==T[3][0:3])
    #print(S[1][3:6]==T[0][0:3])
    #print(S[1][3:6]==T[1][0:3])
    #print(S[1][3:6]==T[2][0:3])
    #print(S[1][3:6]==T[3][0:3])
    #print(S[2][3:6]==T[0][0:3])
    #print(S[2][3:6]==T[1][0:3])
    #print(S[2][3:6]==T[2][0:3])
    #print(S[2][3:6]==T[3][0:3])
    #print(S[3][3:6]==T[0][0:3])
    #print(S[3][3:6]==T[1][0:3])
    #print(S[3][3:6]==T[2][0:3])
    #print(S[3][3:6]==T[3][0:3])
    #print(S[4][3:6]==T[0][0:3])
    #print(S[4][3:6]==T[1][0:3])
    #print(S[4][3:6]==T[2][
