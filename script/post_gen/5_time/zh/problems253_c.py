Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        elif query[0] == '3':
            print(max(s) - min(s))

=======
Suggestion 2

def solve():
    q = int(input())
    s = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            s.append(int(query[2:]))
        elif query[0] == '2':
            x, c = map(int, query[2:].split())
            for j in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))

=======
Suggestion 3

def main():
    from collections import Counter
    from heapq import heappop, heappush
    import sys
    input = sys.stdin.readline

    q = int(input())
    c = Counter()
    hq = []
    s = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c[x] += 1
            s += x
            heappush(hq, x)
        elif query[0] == 2:
            x, c_ = query[1], query[2]
            for _ in range(min(c_, c[x])):
                c[x] -= 1
                s -= x
        else:
            while c[hq[0]] == 0:
                heappop(hq)
            print(hq[-1] - hq[0])

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for j in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        else:
            print(max(s) - min(s))

=======
Suggestion 5

def solve():
    import sys
    import bisect

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))

    S = []
    for i in range(Q):
        if query[i][0] == 1:
            bisect.insort(S, query[i][1])
        elif query[i][0] == 2:
            while query[i][2] > 0:
                if S.count(query[i][1]) == 0:
                    break
                S.remove(query[i][1])
                query[i][2] -= 1
        else:
            print(S[-1] - S[0])

=======
Suggestion 6

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for j in range(query[2]):
                if query[1] in S:
                    S.remove(query[1])
                else:
                    break
        elif query[0] == 3:
            S.sort()
            print(S[-1]-S[0])

=======
Suggestion 7

def main():
    # Q = int(input())
    # q = []
    # for i in range(Q):
    #     q.append(input())
    # print(q)
    # print(q[0])
    # print(q[0].split(' ')[0])
    # print(q[0].split(' ')[1])
    # print(q[0].split(' ')[2])
    # print(q[1])
    # print(q[1].split(' ')[0])
    # print(q[1].split(' ')[1])
    # print(q[1].split(' ')[2])
    # print(q[2])
    # print(q[2].split(' ')[0])
    # print(q[2].split(' ')[1])
    # print(q[2].split(' ')[2])
    # print(q[3])
    # print(q[3].split(' ')[0])
    # print(q[3].split(' ')[1])
    # print(q[3].split(' ')[2])
    # print(q[4])
    # print(q[4].split(' ')[0])
    # print(q[4].split(' ')[1])
    # print(q[4].split(' ')[2])
    # print(q[5])
    # print(q[5].split(' ')[0])
    # print(q[5].split(' ')[1])
    # print(q[5].split(' ')[2])
    # print(q[6])
    # print(q[6].split(' ')[0])
    # print(q[6].split(' ')[1])
    # print(q[6].split(' ')[2])
    # print(q[7])
    # print(q[7].split(' ')[0])
    # print(q[7].split(' ')[1])
    # print(q[7].split(' ')[2])
    # print(q[8])
    # print(q[8].split(' ')[0])
    # print(q[8].split(' ')[1])
    # print(q[8].split(' ')[2])
    q = ['1 3', '1 2', '3', '1 2', '1 7', '3', '2 2 3', '3']
    # q = ['1 10000', '1 1000', '2 100 3', '1 10']
    S = []
    for i in range(len(q)):

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    import sys
    from collections import Counter
    from heapq import heappop, heappush
    input = sys.stdin.readline
    q = int(input())
    s = []
    a = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
            heappush(a, query[1])
        elif query[0] == 2:
            c = query[2]
            count = Counter(s)
            for i in range(min(c, count[query[1]])):
                s.remove(query[1])
            while a and count[a[0]] == 0:
                heappop(a)
        else:
            print(a[0] - s[0])

=======
Suggestion 10

def main():
    q = int(input())
    s = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            count = 0
            for j in range(len(s)):
                if s[j] == x:
                    s.pop(j)
                    count += 1
                    if count == c:
                        break
        elif query[0] == '3':
            print(max(s) - min(s))
