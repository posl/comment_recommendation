Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    #print(s)
    #print(t)
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)
    return 0

=======
Suggestion 2

def main():
    # 读取输入
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    # 逐个检查
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j][-3:]:
                count += 1
                break
    print(count)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j] or s[i][4:6] == t[j] or s[i][5] == t[j]:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [input() for i in range(n)]
    b = [input() for i in range(m)]
    c = 0
    for i in a:
        for j in b:
            if i[-3:] == j:
                c += 1
    print(c)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #N, M = map(int, input().split())
    #S = [input() for _ in range(N)]
    #T = [input() for _ in range(M)]
    S = ['000000', '123456', '987111', '000000']
    T = ['000', '111', '999', '111']
    ans = 0
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)
