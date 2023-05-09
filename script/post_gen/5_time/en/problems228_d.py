Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = 2 ** 20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 2

def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 3

def main():
    N = 2**20
    A = [-1] * N
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

=======
Suggestion 4

def main():
    n = 2 ** 20
    q = int(input())
    a = [-1] * n
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 5

def solve():
    N = 2 ** 20
    A = [-1] * N
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        x %= N
        if t == 1:
            while A[x] != -1:
                x += 1
                x %= N
            A[x] = x
        else:
            print(A[x])

=======
Suggestion 6

def solve():
    n = 2**20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])

=======
Suggestion 7

def main():
    n = 1048576
    q = int(input())
    a = [-1] * n
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % n] != -1:
                h += 1
            a[h % n] = x
        else:
            print(a[x % n])
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = [-1] * 1048576
    for i in range(n):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h % 1048576] != -1:
                h += 1
            a[h % 1048576] = x
        else:
            print(a[x % 1048576])

=======
Suggestion 9

def solve():
    n = 2**20
    q = int(input())
    a = [-1]*n
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while a[h%n] != -1:
                h += 1
            a[h%n] = x
        else:
            print(a[x%n])

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from bisect import bisect_left
    from bisect import bisect_right

    class BIT():
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.data[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.n:
                self.data[i] += x
                i += i & -i

        def lower_bound(self, x):
            if x <= 0:
                return 0
            i = 0
            k = 1 << self.n.bit_length()
            while k > 0:
                if i + k <= self.n and self.data[i + k] < x:
                    x -= self.data[i + k]
                    i += k
                k //= 2
            return i + 1

        def debug(self):
            print(self.data)

    N = 2 ** 20
    bit = BIT(N)
    d = defaultdict(lambda: -1)
    Q = int(input())
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while d[h % N] != -1:
                h += 1
            d[h % N] = x
            bit.add(h % N + 1, 1)
        else:
            if bit.sum(x % N + 1) == 0:
                print(-1)
            else:
                print(d[bisect_left(bit.data, x % N + 1) - 1])

main()
