Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    continue
                else:
                    break
            else:
                ans += 1
    print(ans)
solve()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
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
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if all(s[i][k] == 'o' or s[j][k] == 'o' for k in range(m)):
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    if k == m - 1:
                        ans += 1
                    else:
                        continue
                else:
                    break
    print(ans)

=======
Suggestion 5

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
Suggestion 6

def main():
    n, m = map(int, input().split())
    l = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            cnt = 0
            for k in range(m):
                if l[i][k] == "o" or l[j][k] == "o":
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i].count('o') + s[j].count('o') == m:
                count += 1
    print(count)

main()

=======
Suggestion 8

def is_pair_solved(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] == 'o' or s2[i] == 'o':
            continue
        else:
            return False
    return True
