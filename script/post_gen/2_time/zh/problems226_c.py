Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    #序列长度为key,序列为value
    seq_dict = {}
    #序列长度为key,序列数量为value
    seq_len_dict = {}
    for i in range(n):
        seq = list(map(int, input().split()))[1:]
        seq_len = len(seq)
        if seq_len in seq_dict:
            if seq not in seq_dict[seq_len]:
                seq_dict[seq_len].append(seq)
                seq_len_dict[seq_len] += 1
        else:
            seq_dict[seq_len] = []
            seq_dict[seq_len].append(seq)
            seq_len_dict[seq_len] = 1
    result = 0
    for value in seq_len_dict.values():
        result += value
    print(result)

=======
Suggestion 2

def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = input().split()
        s.add(tuple(l[1:]))
    print(len(s))

=======
Suggestion 3

def main():
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split()))[1:])
    print(len(set([tuple(i) for i in l])))

=======
Suggestion 4

def main():
    n = int(input())
    S = set()
    for i in range(n):
        L = list(map(int, input().split()))
        S.add(tuple(L[1:]))
    print(len(S))

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()[1:])))
    A.sort()
    ans = 1
    for i in range(N - 1):
        if A[i] != A[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    d = {}
    for _ in range(n):
        l = int(input())
        a = tuple(map(int, input().split()))
        if a not in d:
            d[a] = 0
        d[a] += 1
    print(len(d))

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    N = int(input())
    seq = []
    for _ in range(N):
        seq.append(list(map(int, input().split()))[1:])
    print(len(set(map(tuple, seq))))

=======
Suggestion 10

def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = input().split()
        l = l[1:]
        s.add(tuple(l))
    print(len(s))
