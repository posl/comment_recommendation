Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    for i in range(1,m-n+2):
        print(i,end=" ")
        for j in range(1,n):
            print(i+j,end=" ")
        print()

=======
Suggestion 2

def f(n, m, a, i):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m+1):
        a[i] = j
        f(n, m, a, i+1)

n, m = map(int, input().split())
a = [0] * n
f(n, m, a, 0)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [1 for _ in range(n)]
    while True:
        print(*a)
        for i in range(n-1, -1, -1):
            if a[i] < m:
                a[i] += 1
                break
            else:
                a[i] = 1
        else:
            break

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    for i in range(1,m+1):
        if i > n:
            break
        else:
            for j in range(i+1,m+1):
                if j > n:
                    break
                else:
                    for k in range(j+1,m+1):
                        if k > n:
                            break
                        else:
                            print(i,j,k)

=======
Suggestion 5

def main():
    n,m = map(int, input().split())

    for i in range(1, m+1):
        for j in range(1, m+1):
            if i >= j:
                continue
            for k in range(1, m+1):
                if j >= k:
                    continue
                print(i, j, k)

=======
Suggestion 6

def rec(i, m, n, a):
  if i == n:
    print(' '.join(map(str, a)))
    return
  for j in range(1, m+1):
    a[i] = j
    rec(i+1, m, n, a)

=======
Suggestion 7

def dfs(i, n, m, a):
    if i == n:
        print(' '.join(map(str, a)))
        return
    for j in range(1, m+1):
        if i == 0:
            a[i] = j
            dfs(i+1, n, m, a)
        else:
            if a[i-1] < j:
                a[i] = j
                dfs(i+1, n, m, a)

=======
Suggestion 8

def main():
    n,m=map(int,input().split())
    a=[1]*n
    while True:
        print(*a)
        if a[-1]==m:
            for i in range(n-1,-1,-1):
                if a[i]!=m:
                    a[i]+=1
                    for j in range(i+1,n):
                        a[j]=a[i]
                    break
            else:
                break
        else:
            a[-1]+=1

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(1,m+1):
        a.append(i)
    for i in range(1,n):
        a.append(a[-1]+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(a[j-1],end="")
            if j==n:
                print()
            else:
                print(" ",end="")
        a[-j] += 1
        for k in range(n-1):
            if a[-j+k] == m+1:
                a[-j+k] = 1
                a[-j+k+1] += 1
    return 0

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        if i > N:
            print(i)
        else:
            print(i, end=' ')
