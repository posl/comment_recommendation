Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(n, m, path, result):
    if len(path) == n:
        result.append(path)
        return
    for i in range(1, m+1):
        if len(path) == 0 or i > path[-1]:
            dfs(n, m, path+[i], result)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    res = []
    for i in range(1, M + 1):
        res.append([i])
    for i in range(2, N + 1):
        res2 = []
        for j in range(len(res)):
            for k in range(res[j][-1] + 1, M + 1):
                res2.append(res[j] + [k])
        res = res2
    for i in range(len(res)):
        print(' '.join(map(str, res[i])))

=======
Suggestion 3

def print_all_increasing_sequences(n,m):
    print_all_increasing_sequences2(n,m,1,[])

=======
Suggestion 4

def print_list(lst):
    for i in lst:
        print(i, end=' ')
    print()

=======
Suggestion 5

def print_seq(n, m):
    if n == 1:
        for i in range(1, m+1):
            print(i)
    else:
        for i in range(1, m+1):
            print(i)
            print_seq(n-1, i+1)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    A = []
    for i in range(1,M+1):
        A.append(i)
    print(A)

    for i in range(1,M+1):
        for j in range(i+1,M+1):
            print(i,j)
            if j-i == N-1:
                print(i,j)
                break


solve()

=======
Suggestion 7

def print_all_sequences(n, m):
    sequence = []
    print_sequences(n, m, sequence)

=======
Suggestion 8

def print_sequence(n, m):
    sequence = [0] * n
    print_sequence_rec(n, m, 0, sequence)

=======
Suggestion 9

def print_sequence(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        for i in range(1, m + 1):
            if len(seq) == 0 or i > seq[-1]:
                seq.append(i)
                print_sequence(n, m, seq)
                seq.pop()

=======
Suggestion 10

def print_seq(n,m):
    if n == 1:
        for i in range(1,m+1):
            print i
    else:
        for i in range(1,m-n+2):
            for j in print_seq(n-1,m-i):
                print i,j
