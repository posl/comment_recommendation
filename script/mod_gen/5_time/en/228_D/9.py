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

if __name__ == '__main__':
    main()