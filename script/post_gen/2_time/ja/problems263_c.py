Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        if N == 1:
            print(i)
        else:
            for j in range(i+1, M+1):
                if N == 2:
                    print(i, j)
                else:
                    for k in range(j+1, M+1):
                        if N == 3:
                            print(i, j, k)
                        else:
                            for l in range(k+1, M+1):
                                if N == 4:
                                    print(i, j, k, l)
                                else:
                                    for m in range(l+1, M+1):
                                        if N == 5:
                                            print(i, j, k, l, m)
                                        else:
                                            for n in range(m+1, M+1):
                                                if N == 6:
                                                    print(i, j, k, l, m, n)
                                                else:
                                                    for o in range(n+1, M+1):
                                                        if N == 7:
                                                            print(i, j, k, l, m, n, o)
                                                        else:
                                                            for p in range(o+1, M+1):
                                                                if N == 8:
                                                                    print(i, j, k, l, m, n, o, p)
                                                                else:
                                                                    for q in range(p+1, M+1):
                                                                        if N == 9:
                                                                            print(i, j, k, l, m, n, o, p, q)
                                                                        else:
                                                                            for r in range(q+1, M+1):
                                                                                if N == 10:
                                                                                    print(i, j, k, l, m, n, o, p, q, r)

=======
Suggestion 2

def dfs(s):
    if len(s) == N:
        print(*s)
        return
    for i in range(s[-1],M+1):
        dfs(s+[i])

N,M = map(int,input().split())
for i in range(1,M+1):
    dfs([i])

=======
Suggestion 3

def dfs(arr, n, m):
    if len(arr) == n:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, m+1):
        if len(arr) == 0 or arr[-1] < i:
            arr.append(i)
            dfs(arr, n, m)
            arr.pop()

=======
Suggestion 4

def rec(a):
    if len(a)==N:
        print(*a)
        return
    if len(a)==0:
        for i in range(1,M+1):
            rec(a+[i])
    else:
        for i in range(a[-1],M+1):
            rec(a+[i])
N,M=map(int,input().split())
rec([])

=======
Suggestion 5

def dfs(n, m, l):
    if n == 0:
        print(*l)
        return
    if len(l) == 0:
        for i in range(1, m + 1):
            dfs(n - 1, m, l + [i])
    else:
        for i in range(l[-1], m + 1):
            dfs(n - 1, m, l + [i])

n, m = map(int, input().split())
dfs(n, m, [])

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        print(i,end=" ")
    print()
    for i in range(2,N+1):
        for j in range(1,M+1):
            if j == 1:
                print(i,end=" ")
            else:
                print(0,end=" ")
        print()
    return

=======
Suggestion 7

def dfs(l):
    if len(l) == n:
        print(*l)
        return
    for i in range(1,m+1):
        if len(l) == 0:
            dfs(l + [i])
        elif l[-1] < i:
            dfs(l + [i])

n,m = map(int,input().split())
dfs([])

=======
Suggestion 8

def dfs(n, m, a, ans):
    if len(a) == n:
        ans.append(a)
    else:
        for i in range(1, m+1):
            if len(a) == 0 or a[-1] < i:
                dfs(n, m, a+[i], ans)

=======
Suggestion 9

def rec(arr, n, m):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, m+1):
        if len(arr) == 0:
            rec(arr+[i], n, m)
        elif arr[-1] < i:
            rec(arr+[i], n, m)

n, m = list(map(int, input().split()))
rec([], n, m)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        dfs(i, N, M)
