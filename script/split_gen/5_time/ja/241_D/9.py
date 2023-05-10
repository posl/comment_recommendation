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
