Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if query[1] in A:
                A.sort()
                print(A[-query[2]] if len(A) >= query[2] else -1)
            else:
                print(-1)
        elif query[0] == 3:
            if query[1] in A:
                A.sort()
                print(A[query[2]-1] if len(A) >= query[2] else -1)
            else:
                print(-1)
        else:
            print("error")
    return

=======
Suggestion 2

def solve():
    import sys
    input = sys.stdin.readline
    from collections import Counter

    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
            self.el = [0] * (n + 1)

        def add(self, p, x):
            assert (0 <= p < self.n)
            p += 1
            self.el[p] += x
            while p <= self.n:
                self.data[p] += x
                p += p & -p

        def get(self, p):
            assert (0 <= p < self.n)
            p += 1
            s = 0
            while p:
                s += self.data[p]
                p -= p & -p
            return s

        def getsum(self, l, r):
            return self.get(r - 1) - self.get(l - 1)

        def lower_bound(self, x):
            if x <= 0:
                return 0
            i = 0
            k = 1 << self.n.bit_length()
            while k:
                if i + k <= self.n and self.data[i + k] < x:
                    x -= self.data[i + k]
                    i += k
                k >>= 1
            return i + 1

        def debug(self):
            print(self.el)

    class BIT2:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
            self.el = [0] * (n + 1)

        def add(self, p, x):
            assert (0 <= p < self.n)
            p += 1
            self.el[p] += x
            while p <= self.n:
                self.data[p] += x
                p += p & -p

        def get(self, p):
            assert (0 <= p < self.n)
            p += 1
            s = 0
            while p:
                s += self.data[p]
                p -= p & -p
            return s

        def getsum(self, l, r):
            return self.get(r - 1) - self.get(l - 1)

        def lower_bound(self, x):
            if x <= 0:
                return 0

=======
Suggestion 3

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                print(sorted(A[:query[2]], reverse=True)[query[1]-1])
        elif query[0] == 3:
            if len(A) < query[2]:
                print(-1)
            else:
                print(sorted(A[query[2]-1:], reverse=False)[query[1]-1])
        else:
            print('Error')

=======
Suggestion 4

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            if len(a) < query[2]:
                print(-1)
            else:
                a.sort()
                print(a[-query[2]])
        elif query[0] == 3:
            if len(a) < query[2]:
                print(-1)
            else:
                a.sort()
                print(a[query[2]-1])

=======
Suggestion 5

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if a <= x:
                    count += 1
            if count < k:
                print(-1)
            else:
                B = []
                for a in A:
                    if a <= x:
                        B.append(a)
                B.sort(reverse=True)
                print(B[k-1])
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if a >= x:
                    count += 1
            if count < k:
                print(-1)
            else:
                B = []
                for a in A:
                    if a >= x:
                        B.append(a)
                B.sort()
                print(B[k-1])

=======
Suggestion 6

def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while r - l >= 0:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return l

=======
Suggestion 7

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort(reverse=True)
            if query[1] not in A:
                print(-1)
            else:
                print(A.index(query[1])+1)
        elif query[0] == 3:
            A.sort()
            if query[1] not in A:
                print(-1)
            else:
                print(A.index(query[1])+1)
        else:
            print('error')

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x,k = int(query[1]),int(query[2])
            a.sort()
            if a.count(x) < k:
                print(-1)
            else:
                print(a[-k])
        elif query[0] == '3':
            x,k = int(query[1]),int(query[2])
            a.sort()
            if a.count(x) < k:
                print(-1)
            else:
                print(a[k-1])

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a.append(q[1])
        elif q[0] == 2:
            if len(a) < q[2]:
                print(-1)
            else:
                b = sorted(a)
                print(b[-q[2]])
        elif q[0] == 3:
            if len(a) < q[2]:
                print(-1)
            else:
                b = sorted(a)
                print(b[q[2]-1])

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
        def add(self, i, x):
            i += 1
            while i <= self.n:
                self.data[i] += x
                i += i & -i
        def sum(self, i):
            i += 1
            ret = 0
            while i > 0:
                ret += self.data[i]
                i -= i & -i
            return ret
        def bisect_left(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.n.bit_length() - 1)
            while k > 0:
                if x + k <= self.n and self.data[x + k] < w:
                    w -= self.data[x + k]
                    x += k
                k //= 2
            return x
    n = int(input())
    a = []
    d = defaultdict(int)
    for _ in range(n):
        q, *b = map(int, input().split())
        if q == 1:
            a.append(b[0])
            d[b[0]] += 1
        elif q == 2:
            x, k = b
            if d[x] < k:
                print(-1)
            else:
                print(sorted(a).index(x) + k - 1)
        else:
            x, k = b
            if d[x] < k:
                print(-1)
            else:
                print(sorted(a).index(x) - k + 1)
