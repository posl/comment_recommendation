Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, inpu

=======
Suggestion 2

def solve():
    from collections import defaultdict
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline

    q = int(input())
    s = []
    sdict = defaultdict(int)
    smin = []
    smax = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
            sdict[query[1]] += 1
        elif query[0] == 2:
            x, c = query[1], query[2]
            while c > 0:
                if sdict[x] == 0:
                    break
                sdict[x] -= 1
                c -= 1
            if sdict[x] == 0:
                sdict.pop(x)
        else:
            while sdict[s[0]] == 0:
                s.pop(0)
            while sdict[s[-1]] == 0:
                s.pop()
            print(s[-1] - s[0])

=======
Suggestion 3

def solve():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    Q = int(input())
    S = []
    C = Counter()

    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            S.append(x)
            C[x] += 1
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for _ in range(min(c, C[x])):
                S.remove(x)
            C[x] -= min(c, C[x])
        else:
            print(max(S) - min(S))

=======
Suggestion 4

def main():
    # 读取输入
    n = int(input())
    queries = []
    for i in range(n):
        queries.append(input().split())
    # print(queries)
    # 处理
    s = []
    for i in range(n):
        if queries[i][0] == '1':
            s.append(int(queries[i][1]))
        elif queries[i][0] == '2':
            num = int(queries[i][1])
            count = int(queries[i][2])
            for j in range(count):
                s.remove(num)
        elif queries[i][0] == '3':
            s.sort()
            print(s[-1] - s[0])
        else:
            pass

=======
Suggestion 5

def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline

    q = int(input())
    s = []
    c = Counter()
    hq = []
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            s.append(x)
            c[x] += 1
        elif query[0] == '2':
            x = int(query[1])
            m = min(int(query[2]), c[x])
            c[x] -= m
            for _ in range(m):
                heappush(hq, x)
        else:
            while hq and c[hq[0]] == 0:
                heappop(hq)
            print(hq[-1] - hq[0])

=======
Suggestion 6

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(c):
                if x in a:
                    a.remove(x)
                else:
                    break
        else:
            print(max(a)-min(a))

=======
Suggestion 7

def find_min_max(s):
    min = s[0]
    max = s[0]
    for i in range(len(s)):
        if s[i] < min:
            min = s[i]
        if s[i] > max:
            max = s[i]
    return max - min

=======
Suggestion 8

def main():
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    # print(queries)
    # print(q)
    s = []
    for i in range(q):
        if queries[i][0] == 1:
            s.append(queries[i][1])
        elif queries[i][0] == 2:
            for j in range(min(queries[i][2], s.count(queries[i][1]))):
                s.remove(queries[i][1])
        elif queries[i][0] == 3:
            print(max(s) - min(s))

=======
Suggestion 9

def main():
    # 读取输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())

    # 处理
    s = []
    for query in queries:
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for i in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        elif query[0] == '3':
            print(max(s) - min(s))

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            c = int(query[2])
            for j in range(c):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
                else:
                    break
        else:
            print(max(s) - min(s))
