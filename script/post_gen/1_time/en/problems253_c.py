Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for j in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])
        elif query[0] == 3:
            print(max(S) - min(S))

=======
Suggestion 2

def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            S = [x for x in S if x != int(query[1])]
        else:
            print(max(S) - min(S))

=======
Suggestion 3

def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], s.count(query[1]))):
                s.remove(query[1])
        elif query[0] == 3:
            print(max(s) - min(s))

=======
Suggestion 4

def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for i in range(query[2]):
                if query[1] in S:
                    S.remove(query[1])
        else:
            print(max(S)-min(S))

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    S = []
    for q in query:
        if q[0] == 1:
            S.append(q[1])
        elif q[0] == 2:
            if q[2] >= S.count(q[1]):
                S = [s for s in S if s != q[1]]
            else:
                for _ in range(q[2]):
                    S.remove(q[1])
        else:
            print(max(S) - min(S))
    return

=======
Suggestion 6

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    S = defaultdict(int)
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            S[int(query[1])] += 1
        elif query[0] == '2':
            S[int(query[1])] -= int(query[2])
            if S[int(query[1])] <= 0:
                del S[int(query[1])]
        else:
            print(max(S.keys()) - min(S.keys()))

=======
Suggestion 7

def main():
    import sys
    from heapq import heappush, heappop, heapify
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = []
    for i in range(N):
        if A[i][0] == 1:
            heappush(S, A[i][1])
        elif A[i][0] == 2:
            while A[i][2] > 0:
                if S[0] == A[i][1]:
                    heappop(S)
                    A[i][2] -= 1
                else:
                    break
        else:
            print(S[-1] - S[0])
main()

=======
Suggestion 8

def main():
    import sys
    import heapq
    input = sys.stdin.readline
    Q = int(input())
    S = []
    heapq.heapify(S)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(S, query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])
        else:
            print(heapq.nlargest(1, S)[0] - heapq.nsmallest(1, S)[0])

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    S = defaultdict(int)
    for q in query:
        if q[0] == 1:
            S[q[1]] += 1
        elif q[0] == 2:
            if S[q[1]] > 0:
                S[q[1]] -= min(q[2], S[q[1]])
        else:
            print(max(S.keys()) - min(S.keys()))
    return

=======
Suggestion 10

def main():
    from collections import defaultdict
    import sys
    f = sys.stdin
    #f = open("test.txt")
    N = int(f.readline().strip())
    A = [tuple(map(int,f.readline().strip().split())) for i in range(N)]
    D = defaultdict(int)
    S = set()
    for i in range(N):
        if A[i][0] == 1:
            D[A[i][1]] += 1
            S.add(A[i][1])
        elif A[i][0] == 2:
            if D[A[i][1]] > 0:
                D[A[i][1]] -= min(D[A[i][1]],A[i][2])
                if D[A[i][1]] == 0:
                    S.remove(A[i][1])
        else:
            print(max(S)-min(S))
    return
