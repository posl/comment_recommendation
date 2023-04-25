Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
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
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            cnt = 0
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if [S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)] == [True] * M:
                count += 1
    print(count)

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            cnt = 0
            for k in range(M):
                if S[i][k] == "o" or S[j][k] == "o":
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)

=======
Suggestion 8

def get_input():
    n,m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n,m,s
