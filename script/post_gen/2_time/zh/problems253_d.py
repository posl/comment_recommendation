Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    s = []
    for i in range(q):
        query = input().split()
        if int(query[0]) == 1:
            s.append(int(query[1]))
        elif int(query[0]) == 2:
            for i in range(int(query[2])):
                if int(query[1]) in s:
                    s.remove(int(query[1]))
        elif int(query[0]) == 3:
            print(max(s)-min(s))

=======
Suggestion 2

def main():
    #n = int(input())
    #a = [0]*n
    #for i in range(n):
    #    a[i] = int(input())
    #a.sort()
    #print(a[-1]-a[0])
    #print(a)
    #print(a[-1])
    #print(a[0])

    q = int(input())
    a = []
    for i in range(q):
        query = input()
        if query[0] == "1":
            a.append(int(query.split()[1]))
        elif query[0] == "2":
            x, c = map(int, query.split()[1:])
            for j in range(min(c, a.count(x))):
                a.remove(x)
        else:
            a.sort()
            print(a[-1]-a[0])

=======
Suggestion 3

def solve():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    Q = int(input())
    S = []
    cnt = defaultdict(int)
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            heappush(S, int(query[1]))
            cnt[int(query[1])] += 1
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            while c > 0:
                if S[0] == x:
                    heappop(S)
                    cnt[x] -= 1
                    c -= 1
                else:
                    break
        else:
            while cnt[S[0]] == 0:
                heappop(S)
            print(S[-1] - S[0])
solve()

=======
Suggestion 4

def main():
    # 读取输入
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))

    # 问题求解
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(min(query[i][2], S.count(query[i][1]))):
                S.remove(query[i][1])
        else:
            print(max(S) - min(S))

=======
Suggestion 5

def main():
    import sys
    import bisect
    input = sys.stdin.readline
    n = int(input())
    a = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            bisect.insort_left(a, int(query[1]))
        elif query[0] == '2':
            for _ in range(min(int(query[2]), a.count(int(query[1])))):
                a.remove(int(query[1]))
        else:
            print(a[-1] - a[0])

=======
Suggestion 6

def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            count = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == x:
                    s.pop(i)
                    count += 1
                    if count == c:
                        break
        else:
            print(max(s) - min(s))

=======
Suggestion 7

def solve():
    from collections import Counter
    from heapq import heappush, heappop
    from bisect import bisect_left, bisect_right
    import sys
    input = sys.stdin.readline

    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 1回目のクエリの処理
    c = Counter()
    minheap = []
    maxheap = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap, q[1])
            heappush(maxheap, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            break
    # 2回目のクエリの処理
    minheap2 = []
    maxheap2 = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap2, q[1])
            heappush(maxheap2, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            break

    ans = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap2, q[1])
            heappush(maxheap2, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            ans.append(-maxheap2[0] - minheap2[0])
    print('\n'.join(map(str, ans)))
solve()

=======
Suggestion 8

def main():
    q = int(input())
    query = []

    for i in range(q):
        query.append(list(map(int, input().split())))

    S = []
    for i in range(q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            x = query[i][1]
            c = query[i][2]
            count = 0
            for j in range(len(S)):
                if S[j] == x:
                    count += 1
                    if count == c:
                        S.pop(j)
                        break
        elif query[i][0] == 3:
            print(max(S) - min(S))

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    ans = []
    for i in range(N):
        if A[i][0] == 1:
            ans.append(A[i][1])
        elif A[i][0] == 2:
            tmp = []
            for j in range(len(ans)):
                if ans[j] == A[i][1]:
                    tmp.append(j)
            for j in range(A[i][2]):
                ans.pop(tmp.pop())
        elif A[i][0] == 3:
            print(max(ans) - min(ans))

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        query = input().split()
        if query[0] == "1":
            s.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for i in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))
