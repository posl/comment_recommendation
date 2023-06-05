def main():
    from collections import defaultdict
    from heapq import heappush, heappop
    from sys import stdin
    input = stdin.readline
    class Heap:
        def __init__(self):
            self.__heap = []
            self.__counter = defaultdict(int)
        def push(self, x):
            heappush(self.__heap, x)
            self.__counter[x] += 1
        def pop(self):
            while self.__heap:
                x = heappop(self.__heap)
                if self.__counter[x] > 0:
                    self.__counter[x] -= 1
                    return x
            return None
        def __len__(self):
            return len(self.__heap)
    q = int(input())
    h = Heap()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            h.push(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], h.__counter[query[1]])):
                h.pop()
        else:
            print(h.pop() - h.pop())
