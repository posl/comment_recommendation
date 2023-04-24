Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ok = True
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    continue
                ok = False
            if ok:
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
            c = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    c += 1
            if c == m:
                ans += 1
    print(ans)

=======
Suggestion 3

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
main()

=======
Suggestion 4

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
Suggestion 5

def solve():
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
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            flag = True
            for k in range(M):
                if S[i][k] != S[j][k]:
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if sum([S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)]) == M:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            cnt = 0
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    problems = [input() for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if all(problems[i][k] == "o" or problems[j][k] == "o" for k in range(m)):
                count += 1

    print(count)

=======
Suggestion 10

def read_ints():
  return [int(x) for x in input().split()]
