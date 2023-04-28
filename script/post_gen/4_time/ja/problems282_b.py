Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def solve():
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
Suggestion 3

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

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if len(set(S[i]+S[j])) == 1:
                cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    count += 1
            if count == m:
                ans += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    pass
                else:
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

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
solve()

=======
Suggestion 8

def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] == 'x' and s2[i] == 'x':
            return False
    return True

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if check(s[i], s[j]):
            ans += 1
print(ans)

=======
Suggestion 9

def main():
  # n, m = map(int, input().split())
  # s = [list(input()) for _ in range(n)]
  n, m = 5, 5
  s = [['o','o','o','o','o'],['o','o','o','x','x'],['x','x','o','o','o'],['o','x','o','x','o'],['x','x','x','x','x']]
  ans = 0
  for i in range(n):
    for j in range(i+1,n):
      count = 0
      for k in range(m):
        if s[i][k] == 'o' or s[j][k] == 'o':
          count += 1
      if count == m:
        ans += 1
  print(ans)
