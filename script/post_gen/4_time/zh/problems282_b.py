Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            cnt = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ok = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 3

def get_input():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n,m,s

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    continue
                else:
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    N,M = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    return N,M,S

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [[0]*m for i in range(n)]
    for i in range(n):
        a[i] = list(input())
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if a[i][k] == 'o' or a[j][k] == 'o':
                    continue
                else:
                    flag = False
            if flag:
                ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            cnt = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())

    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ok = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ok = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)
