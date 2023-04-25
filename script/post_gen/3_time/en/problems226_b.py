Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    seqs = []
    for i in range(n):
        seq = list(map(int, input().split()))
        seqs.append(seq[1:])
    seqs.sort()
    count = 1
    for i in range(1, n):
        if seqs[i] != seqs[i-1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    seqs = []
    for i in range(N):
        seq = list(map(int, input().split()))
        seqs.append(seq[1:])
    seqs.sort()
    ans = 1
    for i in range(1, N):
        if seqs[i] != seqs[i - 1]:
            ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    L.sort(key=lambda x: x[1:])
    cnt = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    ans = 1
    prev = A[0]
    for i in range(1, N):
        if prev != A[i]:
            ans += 1
            prev = A[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = [tuple(i) for i in l]
    print(len(set(l)))

=======
Suggestion 6

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort()
    cnt = 1
    for i in range(N-1):
        if seq[i] != seq[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append([int(x) for x in input().split()])
    seq.sort()
    prev = seq[0]
    count = 1
    for i in range(1, n):
        if seq[i] != prev:
            count += 1
            prev = seq[i]
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    A.sort()
    A.append([])
    ans = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    a.sort()
    a.append([0, 0])
    count = 0
    prev = [0, 0]
    for i in range(N+1):
        if a[i] == prev:
            count += 1
        prev = a[i]
    print(N-count)

=======
Suggestion 10

def get_total_sequences(n):
    total_sequences = 0
    for i in range(n):
        s = input()
        total_sequences += int(s.split()[0])
    return total_sequences
