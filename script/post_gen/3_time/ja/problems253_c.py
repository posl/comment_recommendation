Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(query[i][1]):
                if query[i][2] > 0:
                    if query[i][2] > S.count(query[i][1]):
                        S.remove(query[i][1])
                        query[i][2] -= 1
                    else:
                        break
        elif query[i][0] == 3:
            print(max(S) - min(S))

=======
Suggestion 2

def main():
    from sys import stdin
    from collections import defaultdict
    from bisect import bisect_left
    read = stdin.buffer.read
    readline = stdin.buffer.readline
    readlines = stdin.buffer.readlines
    q = int(readline())
    s = defaultdict(int)
    a = []
    for _ in range(q):
        query = list(map(int,readline().split()))
        if query[0] == 1:
            s[query[1]] += 1
            a.append(query[1])
        elif query[0] == 2:
            for i in range(min(query[2],s[query[1]])):
                s[a.pop(bisect_left(a,query[1]))] -= 1
        else:
            print(a[-1] - a[0])

=======
Suggestion 3

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    S = defaultdict(int)
    Smax = 0
    Smin = 0
    for i in range(Q):
        if query[i][0] == 1:
            S[query[i][1]] += 1
            if Smax == 0:
                Smax = query[i][1]
                Smin = query[i][1]
            else:
                if query[i][1] > Smax:
                    Smax = query[i][1]
                if query[i][1] < Smin:
                    Smin = query[i][1]
        elif query[i][0] == 2:
            if S[query[i][1]] >= query[i][2]:
                S[query[i][1]] -= query[i][2]
                if S[query[i][1]] == 0:
                    del S[query[i][1]]
            else:
                del S[query[i][1]]
                if len(S) == 0:
                    Smax = 0
                    Smin = 0
                else:
                    Smax = max(S.keys())
                    Smin = min(S.keys())
        else:
            print(Smax-Smin)

=======
Suggestion 4

def main():
    import sys
    import bisect
    input = sys.stdin.readline

    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    S = []
    for q in query:
        if q[0] == 1:
            bisect.insort_left(S,q[1])
        elif q[0] == 2:
            for _ in range(min(q[2],S.count(q[1]))):
                S.remove(q[1])
        else:
            print(S[-1]-S[0])

=======
Suggestion 5

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]

    d = defaultdict(int)
    d[0] = 1
    d[10**9] = 1
    d_sum = 0
    d_min = 0
    d_max = 10**9

    for q in queries:
        if q[0] == 1:
            d[q[1]] += 1
            d_sum += q[1]
        elif q[0] == 2:
            d[q[1]] -= min(q[2], d[q[1]])
            d_sum -= min(q[2], d[q[1]]) * q[1]
        else:
            print(d_max - d_min)
            d[d_max] -= 1
            d[d_min] -= 1
            d_sum -= d_max
            d_sum += d_min
            if d[d_max] == 0:
                d_max -= 1
            if d[d_min] == 0:
                d_min += 1
            d_sum -= d_max
            d_sum += d_min

=======
Suggestion 6

def main():
    from collections import defaultdict
    from bisect import bisect_left, bisect_right
    from heapq import heappop, heappush, heapify
    from sys import stdin
    input = stdin.readline

    Q = int(input())
    S = []
    S_dict = defaultdict(int)
    S_dict[0] = 0
    S_dict[10**9] = 0
    S.append(0)
    S.append(10**9)
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S.append(query[1])
            S_dict[query[1]] += 1
        elif query[0] == 2:
            num = S_dict[query[1]]
            if num >= query[2]:
                S_dict[query[1]] -= query[2]
            else:
                S_dict[query[1]] = 0
            S_dict[0] += query[2] - num
        else:
            S.sort()
            print(S[-1] - S[0] - S_dict[0])

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    import heapq
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    cnt = Counter()
    minh = []
    maxh = []
    a = 0
    b = 0
    for q in query:
        if q[0] == 1:
            a += 1
            heapq.heappush(minh, q[1])
            heapq.heappush(maxh, -q[1])
        elif q[0] == 2:
            b += 1
            cnt[q[1]] += 1
        else:
            while minh[0] in cnt and cnt[minh[0]] > 0:
                heapq.heappop(minh)
            while -maxh[0] in cnt and cnt[-maxh[0]] > 0:
                heapq.heappop(maxh)
            print(-maxh[0] - minh[0])
            cnt[minh[0]] -= 1
            cnt[-maxh[0]] -= 1

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    from heapq import heappop, heappush
    input = sys.stdin.readline
    q = int(input())
    s = defaultdict(int)
    minheap = []
    maxheap = []
    for _ in range(q):
        query = input().rstrip().split()
        if query[0] == '1':
            x = int(query[1])
            s[x] += 1
            heappush(minheap, x)
            heappush(maxheap, -x)
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            while c > 0 and s[x] > 0:
                s[x] -= 1
                c -= 1
            if s[x] == 0:
                while minheap and s[minheap[0]] == 0:
                    heappop(minheap)
                while maxheap and s[-maxheap[0]] == 0:
                    heappop(maxheap)
        else:
            while minheap and s[minheap[0]] == 0:
                heappop(minheap)
            while maxheap and s[-maxheap[0]] == 0:
                heappop(maxheap)
            print(-maxheap[0]-minheap[0])

=======
Suggestion 9

def main():
    from collections import defaultdict
    from sys import stdin
    input = stdin.readline
    from bisect import bisect_left,bisect_right
    n=int(input())
    q=[]
    for i in range(n):
        q.append(list(map(int,input().split())))
    s=defaultdict(int)
    max_=0
    min_=10**9
    for i in range(n):
        if q[i][0]==1:
            s[q[i][1]]+=1
            max_=max(max_,q[i][1])
            min_=min(min_,q[i][1])
        elif q[i][0]==2:
            cnt=0
            for key in sorted(s.keys()):
                if cnt>=q[i][2]:
                    break
                if key==q[i][1]:
                    if s[key]>=q[i][2]-cnt:
                        s[key]-=q[i][2]-cnt
                        cnt=q[i][2]
                    else:
                        cnt+=s[key]
                        s[key]=0
                elif key>q[i][1]:
                    break
                else:
                    cnt+=s[key]
                    s[key]=0
            max_=max(s.keys())
            min_=min(s.keys())
        elif q[i][0]==3:
            print(max_-min_)
