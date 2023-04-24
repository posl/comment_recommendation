Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            for k in range(j+1, m+1):
                print(i, j, k, sep=' ')

=======
Suggestion 2

def dfs(a, n, m):
    if len(a) == n:
        print(" ".join(map(str, a)))
        return
    for i in range(1, m+1):
        if len(a) == 0 or a[-1] < i:
            a.append(i)
            dfs(a, n, m)
            a.pop()

n, m = map(int, input().split())
dfs([], n, m)

=======
Suggestion 3

def solve(N, M):
    if N == 1:
        for i in range(1, M+1):
            print(i)
        return
    for i in range(1, M+1):
        solve(N-1, M-i)

N, M = map(int, input().split())
solve(N, M)

=======
Suggestion 4

def solve(N, M):
    if N == 1:
        for i in range(1, M+1):
            print(i)
        return
    for i in range(1, M+1):
        for j in solve(N-1, M):
            print(i, *j)

N, M = map(int, input().split())
solve(N, M)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    ans = []
    for i in range(1,m+1):
        ans.append([i])
    for i in range(n-1):
        tmp = []
        for j in range(len(ans)):
            for k in range(ans[j][-1]+1,m+1):
                tmp.append(ans[j]+[k])
        ans = tmp
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 6

def dfs(n, m, a):
    if len(a) == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, m+1):
        if len(a) > 0 and a[-1] >= i:
            continue
        a.append(i)
        dfs(n, m, a)
        a.pop()

=======
Suggestion 7

def dfs(n, m, s, ans):
    if len(s) == n:
        ans.append(s)
        return
    for i in range(1, m+1):
        if len(s) == 0 or s[-1] < i:
            dfs(n, m, s+[i], ans)

=======
Suggestion 8

def dfs(n, m, pre, ans):
    if n == 0:
        print(*ans)
        return
    for i in range(pre + 1, m + 1):
        dfs(n - 1, m, i, ans + [i])

=======
Suggestion 9

def dfs(n,m,k,ans):
    if k==n:
        print(' '.join(map(str,ans)))
        return
    for i in range(ans[-1],m+1):
        ans.append(i)
        dfs(n,m,k+1,ans)
        ans.pop()

=======
Suggestion 10

def dfs(n, m, A):
    if n == 0:
        print(" ".join(map(str, A)))
    else:
        for i in range(1, m + 1):
            if len(A) > 0 and A[-1] > i:
                continue
            A.append(i)
            dfs(n - 1, m, A)
            A.pop()
