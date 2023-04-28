Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = i + 1
    for i in range(N, 0, -1):
        ans[i] = ans[2 * i] + ans[2 * i + 1]
    for i in range(1, 2 * N + 1):
        print(ans[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    ans[1] = 0
    for i in range(n):
        ans[2 * (i + 1)] = ans[a[i]] + 1
        ans[2 * (i + 1) + 1] = ans[2 * (i + 1)]
    for i in range(1, 2 * n + 1):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*(2*n+1)
    for i in range(n):
        ans[a[i]] = i+1
    for i in range(1,2*n+1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = ans[i]
        k = 0
        while j > 0:
            j = j//2
            k += 1
        ans[i] = k-1
    for i in range(1, 2*N+1):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(2*N, 0, -1):
        if ans[i] != 0:
            ans[i//2] = max(ans[i//2], ans[i]+1)
    for i in range(1, 2*N+1):
        print(ans[i]-1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2*n+1)
    for i in range(n):
        ans[a[i]] = i+1
    for i in range(2*n, 0, -1):
        if ans[i] == 0:
            ans[i] = ans[i*2] + ans[i*2+1]
    for i in range(1, 2*n+1):
        print(ans[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = [0]*(2*n+1)
    p[1] = 1
    for i in range(n):
        p[2*i+2] = p[i+1]
        p[2*i+3] = p[i+1]
    for i in range(2*n+1):
        print(p[i+1])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    ans = [0]*(2*n+1)
    for i in range(1, n+1):
        ans[i] = ans[a[i]] + 1
        ans[i*2] = ans[i]
        ans[i*2+1] = ans[i]
    for i in range(1, 2*n+1):
        print(ans[i])

=======
Suggestion 9

def dfs(i, g, v, d):
    v[i] = True
    for j in g[i]:
        if v[j] == False:
            d[j] = d[i] + 1
            dfs(j, g, v, d)

n = int(input())
a = list(map(int, input().split()))
g = [[] for i in range(2*n+1)]
for i in range(n):
    g[a[i]].append(i+1)
    g[a[i]+1].append(i+1)
v = [False]*(2*n+1)
d = [0]*(2*n+1)
dfs(1, g, v, d)
for i in range(1, 2*n+1):
    print(d[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 親の番号を格納する配列
    parents = [0] * (2 * N + 1)

    for i in range(N):
        parents[A[i]] = i + 1

    # 親を遡っていき、親がいなくなるまでの数を出力する
    for i in range(1, 2 * N + 1):
        p = parents[i]
        cnt = 0
        while p > 0:
            p //= 2
            cnt += 1

        print(cnt)
