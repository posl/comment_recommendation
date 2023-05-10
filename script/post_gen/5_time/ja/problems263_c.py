Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    for i in range(n,m+1):
        for j in range(i+1,m+1):
            print(i,j)

=======
Suggestion 2

def list_search(n, m, l):
    if n == 1:
        for i in range(1, m + 1):
            l.append(str(i))
        print(' '.join(l))
    else:
        for i in range(1, m + 1):
            l.append(str(i))
            list_search(n - 1, m, l)
            l.pop()

n, m = map(int, input().split())
l = []
list_search(n, m, l)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    for i in range(1,m+2-n):
        print(i,end=" ")
        for j in range(i+1,m+1):
            print(j,end=" ")
        print()

=======
Suggestion 4

def mk_list(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        ret = []
        for i in range(1, m+1):
            for j in mk_list(n-1, m):
                if j[-1] < i:
                    ret.append(j + [i])
        return ret

n, m = map(int, input().split())
for i in mk_list(n, m):
    print(*i)

=======
Suggestion 5

def f(n, m, a, i):
    if i == n:
        print(" ".join(map(str, a)))
        return
    for j in range(1, m+1):
        a[i] = j
        f(n, m, a, i+1)

n, m = map(int, input().split())
a = [0]*n
f(n, m, a, 0)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ans = []
    def dfs(a):
        if len(a) == n:
            ans.append(a)
            return
        for i in range(1, m+1):
            if len(a) > 0 and i <= a[-1]:
                continue
            dfs(a + [i])
    dfs([])
    for a in ans:
        print(*a)

=======
Suggestion 7

def dfs(n, m, a):
    if len(a) == n:
        print(" ".join(map(str, a)))
        return
    s = a[-1] if a else 1
    for i in range(s, m + 1):
        dfs(n, m, a + [i])

n, m = map(int, input().split())
dfs(n, m, [])

=======
Suggestion 8

def solve():
    from itertools import combinations
    N,M = map(int,input().split())
    for i in combinations(range(1,M+1),N):
        print(*i)
solve()

=======
Suggestion 9

def prob_c():
    N,M = map(int, input().split())
    array = [1]*N
    array[0] = 1
    current = 0
    while True:
        if current == N-1:
            print(*array)
            array[current] += 1
            if array[current] > M:
                array[current] = 1
                current -= 1
            continue
        if array[current] > M:
            array[current] = 1
            current -= 1
            continue
        if array[current] >= array[current+1]:
            array[current] += 1
            continue
        if array[current] < array[current+1]:
            current += 1
            continue
        if current == 0:
            break
    return

prob_c()

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = [0] * n
    def rec(i):
        if i == n:
            print(' '.join(map(str, a)))
            return
        for j in range(1, m + 1):
            a[i] = j
            rec(i + 1)
    rec(0)
