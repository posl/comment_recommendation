def main():
    import sys
    from bisect import bisect_left
    from bisect import bisect_right
    def get_ints(): return map(int, sys.stdin.readline().strip().split())
    def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
    def get_int(): return int(sys.stdin.readline().strip())
    def get_str(): return sys.stdin.readline().strip()
    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
        def add(self, i, w):
            x = i
            while x <= self.n:
                self.data[x] += w
                x += x & -x
        def sum(self, i):
            ret, x = 0, i
            while x > 0:
                ret += self.data[x]
                x -= x & -x
            return ret
    class BIT2D:
        def __init__(self, n):
            self.n = n
            self.data = [BIT(n) for _ in range(n + 1)]
        def add(self, i, j, w):
            x = i
            while x <= self.n:
                self.data[x].add(j, w)
                x += x & -x
        def sum(self, i, j):
            ret, x = 0, i
            while x > 0:
                ret += self.data[x].sum(j)
                x -= x & -x
            return ret
    n = get_int()
    a = []
    for _ in range(n):
        t, *args = get_ints()
        if t == 1:
            a.append(args[0])
    a.sort()
    bit = BIT(n)
    for i, v in enumerate(a):
        bit.add(i + 1, v)
    bit2d = BIT2D(n)
    for i, v in enumerate(a):
        bit2d.add(i + 1, bisect_left(a, v), 1)
    q = get_int()
    for _ in range(q):
        t, *args = get_ints()
        if t == 1:
            v = args[0]
            i = bisect_left(a, v)
            a.insert(i, v)
            bit.add(i + 1, v)
            bit
