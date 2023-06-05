Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for j in range(query[2]):
                if query[1] in s:
                    s.remove(query[1])
        elif query[0] == 3:
            print(max(s)-min(s))

=======
Suggestion 2

def main():
    import sys
    from collections import Counter
    from heapq import heapify, heappop, heappush

    def query1(x):
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
            heappush(q, x)

    def query2(x, count):
        while count > 0:
            if x == q[0]:
                heappop(q)
                c[x] -= 1
                if c[x] == 0:
                    del c[x]
            else:
                c[x] -= 1
                heappush(q, x)
            count -= 1

    def query3():
        return q[-1] - q[0]

    q = []
    c = Counter()
    heapify(q)

    n = int(input())
    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            query1(query[1])
        elif query[0] == 2:
            query2(query[1], query[2])
        else:
            print(query3())

=======
Suggestion 3

def main():
    Q = int(input())
    # query_list = []
    # for i in range(Q):
    #     query = input()
    #     query_list.append(query)
    query_list = [input() for i in range(Q)]
    query_list = [query.split() for query in query_list]
    query_list = [[int(query[0]), query[1:]] for query in query_list]

    S = []
    for query in query_list:
        if query[0] == 1:
            S.append(int(query[1][0]))
        elif query[0] == 2:
            x, c = int(query[1][0]), int(query[1][1])
            for i in range(c):
                if x in S:
                    S.remove(x)
                else:
                    break
        elif query[0] == 3:
            print(max(S) - min(S))

=======
Suggestion 4

def main():
    q = int(input())
    s = []
    for i in range(0,q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            for j in range(0,int(query[2])):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
        elif query[0] == '3':
            print(max(s)-min(s))
        else:
            print('error')

=======
Suggestion 5

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        if arr[i][0] == 1:
            arr.append(arr[i][1])
        if arr[i][0] == 2:
            for j in range(arr[i][2]):
                if arr[i][1] in arr:
                    arr.remove(arr[i][1])
        if arr[i][0] == 3:
            if len(arr) > 0:
                print(max(arr) - min(arr))
            else:
                print("")

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            c = int(query[2])
            x = int(query[1])
            while c > 0:
                if x in s:
                    s.remove(x)
                c -= 1
        elif query[0] == '3':
            print(max(s) - min(s))

=======
Suggestion 7

def main():
    # 读取输入
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(input().split())

    # 处理
    s = []
    for query in queries:
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for _ in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    from bisect import bisect_left, bisect_right

    def input(): return sys.stdin.readline().rstrip()

    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # 値と出現回数を記録する辞書
    value_dict = defaultdict(int)

    # 値のリスト
    value_list = []

    # 値のリストをソート済みに保つためのリスト
    value_list_sorted = []

    # 値のリストの中で、値が何番目に小さいかを管理する辞書
    value_to_index = {}

    # 値のリストの中で、値が何番目に大きいかを管理する辞書
    value_to_index_rev = {}

    # 値のリストに値を追加する
    def add_value(x):
        value_dict[x] += 1
        value_list.append(x)
        value_list_sorted.append(x)

        # 値のリストをソート
        value_list_sorted.sort()

        # 値のリストの中で、値が何番目に小さいかを管理する辞書を更新
        value_to_index[x] = bisect_left(value_list_sorted, x)

        # 値のリストの中で、値が何番目に大きいかを管理する辞書を更新
        value_to_index_rev[x] = bisect_right(value_list_sorted, x) - 1

    # 値のリストから値を削除する
    def remove_value(x):
        value_dict[x] -= 1
        value_list.remove(x)

        # 値のリストの中で、値が何番目に小さいかを管理する辞書を更新
        value_to_index[x] = bisect_left(value_list_sorted, x)

        # 値のリストの中で、値が何番目に大きいかを管理する辞書を更新
        value_to_index_rev[x] = bis

=======
Suggestion 9

def main():
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    #print(query)
    s = []
    for i in range(q):
        if query[i][0] == '1':
            s.append(int(query[i][1]))
        elif query[i][0] == '2':
            for j in range(int(query[i][2])):
                if int(query[i][1]) in s:
                    s.remove(int(query[i][1]))
                else:
                    break
        else:
            print(max(s) - min(s))
    #print(s)

=======
Suggestion 10

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
