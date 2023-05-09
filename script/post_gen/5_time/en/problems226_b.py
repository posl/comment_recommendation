Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        s.add(tuple(l))
    print(len(s))

=======
Suggestion 2

def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = list(map(int, input().split()))
        s.add(tuple(l[1:]))
    print(len(s))

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    a.sort()
    ans = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    L.sort()
    count = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    seq = {}
    for i in range(n):
        l, *a = map(int, input().split())
        seq[tuple(a)] = 1
    print(len(seq))

=======
Suggestion 6

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    seq.sort()
    prev = seq[0]
    count = 1
    for i in range(1, N):
        if seq[i] != prev:
            count += 1
            prev = seq[i]
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    ans = 1
    for i in range(N - 1):
        if L[i] != L[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])
    count = 1
    for i in range(1, n):
        if l[i] != l[i-1]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    seqs = []
    for _ in range(n):
        seqs.append(input().split())
    seqs.sort()
    prev = seqs[0]
    cnt = 1
    for seq in seqs[1:]:
        if seq != prev:
            cnt += 1
        prev = seq
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort()
    print(len(list(k for k, _ in itertools.groupby(seq))))
