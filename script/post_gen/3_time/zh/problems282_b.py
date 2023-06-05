Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
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
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            flag = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    flag = False
            if flag:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    cnt = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    if k == M - 1:
                        cnt += 1
                    continue
                else:
                    break
    print(cnt)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    continue
                else:
                    break
            else:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ok = True
            for k in range(m):
                if s[i][k] == "x" and s[j][k] == "x":
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    count += 1
                    break
    print(count)

=======
Suggestion 9

def solve(n,m,ss):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ok = True
            for k in range(m):
                if ss[i][k] == 'x' and ss[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    return ans
