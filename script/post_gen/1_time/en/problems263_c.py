Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [[i] + j for i in range(1, m + 1) for j in solve(n - 1, m) if i < j[0]]

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        if N == 1:
            print(i)
        else:
            for j in range(i+1, M+2):
                if N == 2:
                    print(i, j)
                else:
                    for k in range(j+1, M+3):
                        if N == 3:
                            print(i, j, k)
                        else:
                            for l in range(k+1, M+4):
                                if N == 4:
                                    print(i, j, k, l)
                                else:
                                    for m in range(l+1, M+5):
                                        if N == 5:
                                            print(i, j, k, l, m)
                                        else:
                                            for n in range(m+1, M+6):
                                                if N == 6:
                                                    print(i, j, k, l, m, n)
                                                else:
                                                    for o in range(n+1, M+7):
                                                        if N == 7:
                                                            print(i, j, k, l, m, n, o)
                                                        else:
                                                            for p in range(o+1, M+8):
                                                                if N == 8:
                                                                    print(i, j, k, l, m, n, o, p)
                                                                else:
                                                                    for q in range(p+1, M+9):
                                                                        if N == 9:
                                                                            print(i, j, k, l, m, n, o, p, q)
                                                                        else:
                                                                            for r in range(q+1, M+10):
                                                                                if N == 10:
                                                                                    print(i, j, k, l, m, n, o, p, q, r)
                                                                                else:
                                                                                    print("Error: N is too large.")

main()

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0]*n
    def dfs(i):
        if i == n:
            print(*a)
            return
        for j in range(1, m+1):
            if i > 0 and a[i-1] >= j:
                continue
            a[i] = j
            dfs(i+1)
    dfs(0)

=======
Suggestion 4

def f(n, m, i, a):
    if i == n:
        print(*a)
    else:
        for j in range(1, m+1):
            if i == 0 or a[i-1] < j:
                a[i] = j
                f(n, m, i+1, a)

n, m = map(int, input().split())
a = [0]*n
f(n, m, 0, a)

=======
Suggestion 5

def seq(n, m, s):
    if n == 0:
        print(' '.join(map(str, s)))
        return
    for i in range(1, m + 1):
        if not s or i > s[-1]:
            s.append(i)
            seq(n - 1, m, s)
            s.pop()

n, m = map(int, input().split())
seq(n, m, [])

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        dfs(i, n - 1, m)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    for i in range(1, m+1):
        dfs(i, 1, n, m)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    l = [i for i in range(1, M + 1)]
    for i in range(1, N + 1):
        for j in range(len(l) - 1, -1, -1):
            if l[j] <= l[-i]:
                l.pop(j)
    for i in range(len(l)):
        print(l[i], end = " ")
        for j in range(N - 1):
            print(l[i] + j + 1, end = " ")
        print("")

=======
Suggestion 9

def dfs(cand, path, n):
    if len(path) == n:
        print(*path)
        return
    for i in range(len(cand)):
        dfs(cand[i+1:], path+[cand[i]], n)

n, m = map(int, input().split())
dfs(list(range(1, m+1)), [], n)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    for i in range(1, M + 1):
        dfs(i, 1, N, [i])
