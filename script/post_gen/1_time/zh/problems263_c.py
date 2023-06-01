Synthesizing 10/10 solutions

=======
Suggestion 1

def func(n, m):
    if n == 1:
        for i in range(1, m+1):
            print(i)
    else:
        for i in range(1, m+1):
            func(n-1, i)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def dfs(n, m, a, i):
    if i == n:
        print(' '.join(map(str, a)))
    else:
        for j in range(1, m + 1):
            a[i] = j
            dfs(n, m, a, i + 1)

=======
Suggestion 4

def print_all_sequences(n, m, a):
    if n == 0:
        print(a)
        return

    for i in range(1, m+1):
        if len(a) > 0 and i <= a[-1]:
            continue

        a.append(i)
        print_all_sequences(n-1, m, a)
        a.pop()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [0] * n
    def dfs(i, x):
        if i == n:
            print(" ".join(map(str, a)))
        else:
            for y in range(x + 1, m + 1):
                a[i] = y
                dfs(i + 1, y)
    dfs(0, 0)

=======
Suggestion 6

def printAll(n, m, prefix):
    if n == 0:
        print(prefix)
    else:
        for i in range(1, m + 1):
            printAll(n - 1, m, prefix + ' ' + str(i))

=======
Suggestion 7

def printSeq(n,m,l):
    if n == 0:
        print(l)
    else:
        for i in range(1,m+1):
            if len(l) == 0 or i > l[-1]:
                l.append(i)
                printSeq(n-1,m,l)
                l.pop()

=======
Suggestion 8

def solve():
    n,m=map(int,input().split())
    a=[1]*n
    def dfs(i):
        if i==n:
            print(*a)
            return
        for j in range(1,m+1):
            a[i]=j
            dfs(i+1)
    dfs(0)
solve()

=======
Suggestion 9

def f(n, m):
    if n == 1:
        for i in range(1, m + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            f(n - 1, i - 1)
            print(i)

f(3, 5)

=======
Suggestion 10

def print_seq(n,m):
    if n == 1:
        return [[i] for i in range(1,m+1)]
    else:
        return [[i]+j for i in range(1,m+1) for j in print_seq(n-1,m) if i > j[0]]
