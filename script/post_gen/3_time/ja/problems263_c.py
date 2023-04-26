Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, n, m, a):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m + 1):
        a[i] = j
        dfs(i + 1, n, m, a)

n, m = map(int, input().split())
a = [0] * n
dfs(0, n, m, a)

=======
Suggestion 2

def f(n,m):
    if n==1:
        return [[i] for i in range(1,m+1)]
    else:
        return [[i] + j for i in range(1,m+1) for j in f(n-1,m) if i>j[0]]

n,m = map(int,input().split())
for i in f(n,m):
    print(*i)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    for i in range(1,m-n+2):
        print(i,end=' ')
        for j in range(1,n):
            print(i+j,end=' ')
        print()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [1] * N
    def dfs(i):
        if i == N:
            print(*A)
            return
        for j in range(A[i - 1], M + 1):
            A[i] = j
            dfs(i + 1)
    dfs(1)

=======
Suggestion 5

def dfs(lst, n, m):
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, m+1):
        if len(lst) > 0 and lst[-1] >= i:
            continue
        dfs(lst+[i], n, m)

n, m = map(int, input().split())
dfs([], n, m)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    ans = []
    for i in range(1,M+1):
        for j in range(1,M+1):
            if i < j:
                ans.append(str(i)+" "+str(j))
    print("\n".join(ans))

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    ans = []
    for i in range(1,M+1):
        ans.append([i])
    for i in range(1,N):
        tmp = []
        for j in ans:
            for k in range(j[-1]+1,M+1):
                tmp.append(j+[k])
        ans = tmp
    for i in ans:
        print(*i)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    
    def dfs(seq):
        if len(seq) == N:
            print(' '.join(map(str, seq)))
            return
        for i in range(seq[-1] + 1, M + 1):
            dfs(seq + [i])
    
    for i in range(1, M + 1):
        dfs([i])
solve()

=======
Suggestion 9

def solve():
    n,m = list(map(int, input().split()))
    ans = []
    def dfs(a):
        if len(a) == n:
            ans.append(a)
            return
        for i in range(1, m+1):
            if a[-1] < i:
                dfs(a+[i])
    for i in range(1, m+1):
        dfs([i])
    for a in ans:
        print(*a)
solve()

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    a = [0 for i in range(n)]
    def f(i):
        if i==n:
            print(*a)
        else:
            for j in range(1, m+1):
                a[i] = j
                if i==0 or a[i-1] < a[i]:
                    f(i+1)
    f(0)
