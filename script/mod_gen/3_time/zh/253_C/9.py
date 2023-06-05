def solve():
    import sys
    from collections import Counter
    from heapq import heappush, heappop
    sys.setrecursionlimit(10 ** 6)
    readline = sys.stdin.buffer.readline
    INF = 10 ** 18
    mod = 10 ** 9 + 7
    class Heapq:
        def __init__(self, arr, reverse=False):
            self.sign = 1
            if reverse:
                self.sign = -1
            self.heap = []
            for i in arr:
                self.heap.append(self.sign * i)
            self.heapify()
        def heapify(self):
            for i in range(len(self.heap) // 2 - 1, -1, -1):
                self.down_heap(i)
        def push(self, x):
            heappush(self.heap, self.sign * x)
        def pop(self):
            return self.sign * heappop(self.heap)
        def down_heap(self, i):
            left = 2 * i + 1
            right = 2 * i + 2
            if left >= len(self.heap):
                return
            if right >= len(self.heap):
                if self.heap[left] < self.heap[i]:
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                return
            if self.heap[left] < self.heap[right]:
                if self.heap[left] < self.heap[i]:
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                    self.down_heap(left)
            else:
                if self.heap[right] < self.heap[i]:
                    self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                    self.down_heap(right)
        def up_heap(self, i):
            if i == 0:
                return
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                self.up_heap(parent)
        def __len__(self):
            return len(self.heap)
    n = int(readline())
    S = Heapq([], reverse=True)
    cnt = Counter()
    for _ in range(n):
        q = list(map(int, readline().split()))
        if q[0] == 1:
            S.push(q[1])
            cnt[q[1]]

if __name__ == '__main__':
    solve()