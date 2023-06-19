Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
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
Suggestion 2

def get_input():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    return N, M, S

=======
Suggestion 3

def solve():
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
solve()

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ok = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    break
            else:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
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
Suggestion 7

def solve():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ok = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

solve()

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n,m=map(int,input().split())
    s=[]
    for i in range(n):
        s.append(input())
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            flag=True
            for k in range(m):
                if s[i][k]=='x' and s[j][k]=='x':
                    flag=False
                    break
            if flag:
                count+=1
    print(count)

=======
Suggestion 10

def main():
    N,M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(list(input()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            flag = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)
