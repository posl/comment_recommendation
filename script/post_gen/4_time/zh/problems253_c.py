Synthesizing 10/10 solutions

=======
Suggestion 1

def min(a,b):
    if a > b:
        return b
    else:
        return a

=======
Suggestion 2

def main():
    Q = int(input())
    S = []
    for i in range(0,Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(0,c):
                if x in S:
                    S.remove(x)
                else:
                    break
        else:
            print(max(S)-min(S))

=======
Suggestion 3

def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            s.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for _ in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s)-min(s))

=======
Suggestion 4

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            if x in S:
                count = 0
                for j in range(len(S)):
                    if S[j] == x:
                        S.pop(j)
                        count += 1
                        if count == c:
                            break
        elif query[0] == '3':
            print(max(S) - min(S))

=======
Suggestion 5

def problem253_c():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    from heapq import heapify

    def solve():
        Q = int(sys.stdin.readline())
        S = defaultdict(int)
        min_heap = []
        max_heap = []
        for _ in range(Q):
            query = sys.stdin.readline().split()
            if query[0] == "1":
                x = int(query[1])
                S[x] += 1
                heappush(min_heap, x)
                heappush(max_heap, -x)
            elif query[0] == "2":
                x = int(query[1])
                c = int(query[2])
                while c > 0 and S[x] > 0:
                    S[x] -= 1
                    c -= 1
                if S[x] == 0:
                    while min_heap and S[min_heap[0]] == 0:
                        heappop(min_heap)
                    while max_heap and S[-max_heap[0]] == 0:
                        heappop(max_heap)
            else:
                while min_heap and S[min_heap[0]] == 0:
                    heappop(min_heap)
                while max_heap and S[-max_heap[0]] == 0:
                    heappop(max_heap)
                print(-max_heap[0] - min_heap[0])

    solve()

=======
Suggestion 6

def main():
    n = int(input())
    q_list = []
    for i in range(n):
        q_list.append(list(map(int, input().split())))
    s = []
    for i in range(n):
        if q_list[i][0] == 1:
            s.append(q_list[i][1])
        elif q_list[i][0] == 2:
            for j in range(q_list[i][2]):
                if q_list[i][1] in s:
                    s.remove(q_list[i][1])
        else:
            s.sort()
            print(s[-1]-s[0])

=======
Suggestion 7

def main():
    q = int(input())
    L = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            L.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for i in range(c):
                if x in L:
                    L.remove(x)
                else:
                    break
        elif query[0] == '3':
            print(max(L) - min(L))

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        a = input().split()
        if a[0] == "1":
            print("insert")
        elif a[0] == "2":
            print("delete")
        else:
            print("print")

=======
Suggestion 10

def main():
    # 读取标准输入
    # 读取第一行的n
    q = int(input())
    # 读取每一行
    for i in range(q):
        # 读取每一行
        line = input().split()
        # 读取每一行
        if line[0] == "1":
            num = int(line[1])
            print(num)
        elif line[0] == "2":
            num = int(line[1])
            print(num)
        elif line[0] == "3":
            print(1)
