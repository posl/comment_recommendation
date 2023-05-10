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

if __name__ == '__main__':
    solve()