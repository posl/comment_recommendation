Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(a, n, m):
    if len(a) == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, m+1):
        if not a or a[-1] < i:
            a.append(i)
            dfs(a, n, m)
            a.pop()

n, m = map(int, input().split())
dfs([], n, m)

This is a sample program to print all strictly increasing integer sequences of length N where all elements are between 1 and M (inclusive), in lexicographically ascending order.

=======
Suggestion 2

def print_sequences(n, m):
    if n == 1:
        for i in range(1, m + 1):
            print(i)
    else:
        for i in range(1, m + 1):
            print_sequences(n - 1, i - 1)
            for j in range(1, m + 1):
                print(i, end=" ")
            print()

n, m = map(int, input().split())
print_sequences(n, m)

=======
Suggestion 3

def solve(n, m):
    if n == 0:
        return
    for i in range(1, m+1):
        if n == 1:
            print(i)
        else:
            for j in solve(n-1, m):
                if i < j[0]:
                    print(i, *j)

=======
Suggestion 4

def printSeq(N, M, seq):
    if N == 0:
        print(*seq)
    else:
        for i in range(1, M+1):
            if len(seq) == 0 or seq[-1] < i:
                printSeq(N-1, M, seq+[i])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    for i in range(1, m+1):
        dfs([i], n, m)

=======
Suggestion 6

def dfs(n, m, depth, s):
    if depth == n:
        print(*s)
        return
    for i in range(1, m+1):
        if not s or s[-1] < i:
            s.append(i)
            dfs(n, m, depth+1, s)
            s.pop()

n, m = map(int, input().split())
dfs(n, m, 0, [])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    for i in range(1, M + 1):
        dfs(N, M, [i])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        print(i, end="")
        if i < m:
            print(" ", end="")
        else:
            print()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [0] * n
    a = [0] * n
    for i in range(n):
        s[i] = i + 1
        a[i] = 1
    while True:
        print(' '.join(map(str, s)))
        i = n - 1
        while i >= 0 and s[i] == m - n + i + 1:
            i -= 1
        if i < 0:
            return
        s[i] += 1
        for j in range(i + 1, n):
            s[j] = s[j - 1] + 1

=======
Suggestion 10

def gen_inc_seq(n, m, seq):
    if n == 0:
        print(*seq)
        return
    for i in range(1, m+1):
        if len(seq) == 0 or seq[-1] < i:
            seq.append(i)
            gen_inc_seq(n-1, m, seq)
            seq.pop()

n, m = map(int, input().split())
gen_inc_seq(n, m, [])
