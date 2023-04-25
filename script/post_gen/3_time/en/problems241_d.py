Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for _ in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A = sorted(A)
            if len(A) >= query[2]:
                print(A[-query[2]])
            else:
                print(-1)
        elif query[0] == 3:
            A = sorted(A)
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
        elif s[0] == '2':
            x = int(s[1])
            k = int(s[2])
            b = [t for t in a if t <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(s[1])
            k = int(s[2])
            b = [t for t in a if t >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])
main()

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for _ in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        line = input().split()
        if line[0] == '1':
            a.append(int(line[1]))
        elif line[0] == '2':
            x = int(line[1])
            k = int(line[2])
            tmp = []
            for j in range(len(a)):
                if a[j] <= x:
                    tmp.append(a[j])
            tmp.sort()
            if len(tmp) < k:
                print(-1)
            else:
                print(tmp[-k])
        else:
            x = int(line[1])
            k = int(line[2])
            tmp = []
            for j in range(len(a)):
                if a[j] >= x:
                    tmp.append(a[j])
            tmp.sort()
            if len(tmp) < k:
                print(-1)
            else:
                print(tmp[k-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for _ in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
        elif s[0] == '2':
            if len(a) == 0:
                print(-1)
            else:
                b = [x for x in a if x <= int(s[1])]
                if len(b) < int(s[2]):
                    print(-1)
                else:
                    b.sort(reverse=True)
                    print(b[int(s[2])-1])
        elif s[0] == '3':
            if len(a) == 0:
                print(-1)
            else:
                b = [x for x in a if x >= int(s[1])]
                if len(b) < int(s[2]):
                    print(-1)
                else:
                    b.sort()
                    print(b[int(s[2])-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        s = input().split()
        if s[0] == '1':
            A.append(int(s[1]))
        elif s[0] == '2':
            x = int(s[1])
            k = int(s[2])
            B = [a for a in A if a <= x]
            if len(B) < k:
                print(-1)
            else:
                print(sorted(B)[-k])
        else:
            x = int(s[1])
            k = int(s[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                print(sorted(B)[k-1])

=======
Suggestion 7

def main():
    # input
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    # compute
    A = []
    for query in queries:
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            cnt = 0
            for a in A:
                if a <= x:
                    cnt += 1
            if cnt < k:
                print(-1)
            else:
                A.sort(reverse=True)
                print(A[k-1])
        else:
            x = int(query[1])
            k = int(query[2])
            cnt = 0
            for a in A:
                if a >= x:
                    cnt += 1
            if cnt < k:
                print(-1)
            else:
                A.sort()
                print(A[k-1])

=======
Suggestion 8

def main():
    from collections import defaultdict
    import bisect
    import sys
    input = sys.stdin.readline
    q = int(input())
    a = []
    d = defaultdict(lambda: 0)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            bisect.insort(a, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            if len(a) == 0 or query[1] < a[0]:
                print(-1)
            else:
                print(a[-query[2]])
        else:
            if len(a) == 0 or query[1] > a[-1]:
                print(-1)
            else:
                print(a[query[2]-1])

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def insert(x):
    global A
    A.append(x)
    A.sort()
