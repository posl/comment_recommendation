Synthesizing 10/10 solutions

=======
Suggestion 1

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = [i for i in range(r)]
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1,r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    for i in range(1,m+1):
        if n==1:
            print(i)
        else:
            for j in range(1,m+1):
                if n==2:
                    print(i,j)
                else:
                    for k in range(1,m+1):
                        if n==3:
                            print(i,j,k)
                        else:
                            for l in range(1,m+1):
                                if n==4:
                                    print(i,j,k,l)
                                else:
                                    for o in range(1,m+1):
                                        if n==5:
                                            print(i,j,k,l,o)
                                        else:
                                            for p in range(1,m+1):
                                                if n==6:
                                                    print(i,j,k,l,o,p)
                                                else:
                                                    for q in range(1,m+1):
                                                        if n==7:
                                                            print(i,j,k,l,o,p,q)
                                                        else:
                                                            for r in range(1,m+1):
                                                                if n==8:
                                                                    print(i,j,k,l,o,p,q,r)
                                                                else:
                                                                    for s in range(1,m+1):
                                                                        if n==9:
                                                                            print(i,j,k,l,o,p,q,r,s)
                                                                        else:
                                                                            for t in range(1,m+1):
                                                                                if n==10:
                                                                                    print(i,j,k,l,o,p,q,r,s,t)

=======
Suggestion 3

def print_all_strictly_increasing_integer_sequences(n, m):
    if n == 0:
        print()
    else:
        for i in range(1, m+1):
            print(i, end=' ')
            print_all_strictly_increasing_integer_sequences(n-1, m)
            print()

=======
Suggestion 4

def get_all_combinations(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [[i] + comb for i in range(1, m + 1) for comb in get_all_combinations(n - 1, m) if i > comb[0]]

n, m = map(int, input().split())
for comb in get_all_combinations(n, m):
    print(*comb)

=======
Suggestion 5

def print_sequences(n, m, sequence):
    if n == 0:
        print(sequence)
        return
    for i in range(1, m + 1):
        print_sequences(n - 1, m, sequence + str(i))

=======
Suggestion 6

def main():
    N, M = map(int, raw_input().split())
    A = [0] * N
    def rec(i, m):
        if i == N:
            print " ".join(map(str, A))
            return
        for j in xrange(m, M + 1):
            A[i] = j
            rec(i + 1, j + 1)
    rec(0, 1)

main()

=======
Suggestion 7

def generate_sequences(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    seqs = []
    for i in range(1, m+1):
        for seq in generate_sequences(n-1, m):
            if seq[-1] < i:
                seqs.append(seq+[i])
    return seqs

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(1, M+1):
        A.append(i)
    import itertools
    for x in itertools.combinations(A, N):
        print(*x)

=======
Suggestion 9

def print_increasing_seq(n, m, seq):
    if len(seq) == n:
        print(" ".join([str(x) for x in seq]))
    else:
        if len(seq) == 0:
            start = 1
        else:
            start = seq[-1] + 1
        for i in range(start, m+1):
            seq.append(i)
            print_increasing_seq(n, m, seq)
            seq.pop()

=======
Suggestion 10

def solution():
    N, M = map(int, input().split())

    def dfs(arr):
        if len(arr) == N:
            print(" ".join(map(str, arr)))
            return

        for i in range(1, M + 1):
            if arr[-1] < i:
                dfs(arr + [i])

    for i in range(1, M + 1):
        dfs([i])


solution()
