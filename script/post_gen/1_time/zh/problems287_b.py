Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(m):
        for j in range(n):
            if t[i] == s[j][3:6]:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
                break
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)
main()

=======
Suggestion 4

def problem287_b():
    n,m = map(int, input().split())
    s_list = []
    for i in range(n):
        s_list.append(input())
    t_list = []
    for i in range(m):
        t_list.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s_list[i][-3:] == t_list[j]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    #print(s)
    #print(t)
    #print(len(s))
    #print(len(t))
    #print(s[0])
    #print(t[0])
    #print(s[0][-3:])
    #print(t[0])
    #print(s[0][-3:] == t[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j][3:6]:
                count += 1
                break
    print(count)
