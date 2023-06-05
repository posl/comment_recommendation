Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()[1:])))

    al = set()
    for i in range(n):
        al.add(tuple(a[i]))
    print(len(al))

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L[1:])

    A.sort()
    ans = 0
    prev = None
    for i in range(N):
        if A[i] != prev:
            ans += 1
            prev = A[i]

    print(ans)

=======
Suggestion 3

def problems226_b():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    ans = []
    for i in range(n):
        if l[i] not in ans:
            ans.append(l[i])
    print(len(ans))

=======
Suggestion 4

def count_different_sequences():
    N = int(input())
    sequences = []
    for i in range(N):
        sequences.append(input().split()[1:])
    #print(sequences)
    #print(len(sequences))
    sequences.sort()
    #print(sequences)
    #print(len(sequences))
    count = 1
    for i in range(1, N):
        if sequences[i] != sequences[i-1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split()))[1:])
    seq.sort()
    count = 1
    for i in range(N-1):
        if seq[i] != seq[i+1]:
            count += 1
    print(count)

=======
Suggestion 6

def input():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    return n, A

=======
Suggestion 7

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split()))[1:])
    print(len(set(map(tuple, seq))))

=======
Suggestion 8

def main():
    n = int(input())
    seqs = {}
    for i in range(n):
        seq = tuple(map(int, input().split()[1:]))
        if seq in seqs:
            seqs[seq] += 1
        else:
            seqs[seq] = 1
    print(len(seqs))

=======
Suggestion 9

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    count = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    for i in range(N):
        L[i] = [int(x) for x in L[i]]
    L.sort()
    count = 1
    for i in range(1,N):
        if(L[i] != L[i-1]):
            count += 1
    print(count)
