Synthesizing 10/10 solutions

=======
Suggestion 1

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
            m = min(c, S.count(x))
            for j in range(m):
                S.remove(x)
        else:
            print(max(S) - min(S))

=======
Suggestion 2

def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            m = min(c, S.count(x))
            for _ in range(m):
                S.remove(x)
        else:
            print(max(S)-min(S))

=======
Suggestion 3

def main():
    Q = int(input())
    S = []
    for q in range(Q):
        query = input().split()
        if query[0] == "1":
            S.append(int(query[1]))
        elif query[0] == "2":
            m = min(int(query[2]), S.count(int(query[1])))
            for i in range(m):
                S.remove(int(query[1]))
        else:
            print(max(S)-min(S))

=======
Suggestion 4

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input()
        if query[0] == "1":
            S.append(int(query[2:]))
        elif query[0] == "2":
            query = query.split(" ")
            x = int(query[1])
            c = int(query[2])
            for j in range(min(c,S.count(x))):
                S.remove(x)
        elif query[0] == "3":
            print(max(S)-min(S))

=======
Suggestion 5

def main():
    Q = int(input())
    S = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 1:
            print(max(S) - min(S))
        elif len(query) == 2:
            S.append(query[1])
        else:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])

=======
Suggestion 6

def main():
    import bisect
    Q = int(input())
    S = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            bisect.insort(S, int(query[1]))
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for _ in range(min(c, S.count(x))):
                S.remove(x)
        else:
            print(S[-1] - S[0])

=======
Suggestion 7

def main():
    Q = int(input())
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            print(x)
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            print(x, c)
        elif query[0] == '3':
            print('3')

=======
Suggestion 8

def main():
    from collections import deque
    import sys
    readline = sys.stdin.readline
    Q = int(readline())
    S = deque([])
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 1:
            S.append(query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], S.count(query[1]))):
                S.remove(query[1])
        else:
            print(max(S) - min(S))

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    q = int(input())
    s = defaultdict(int)
    min_s = 10**9
    max_s = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
            min_s = min(min_s, query[1])
            max_s = max(max_s, query[1])
        elif query[0] == 2:
            s[query[1]] -= min(s[query[1]], query[2])
            if s[query[1]] == 0:
                del s[query[1]]
                if query[1] == min_s:
                    min_s = min(s.keys())
                if query[1] == max_s:
                    max_s = max(s.keys())
        else:
            print(max_s-min_s)
    return

=======
Suggestion 10

def main():
    from collections import defaultdict
    import sys
    readline = sys.stdin.readline

    Q = int(readline())
    S = defaultdict(int)
    minS = 10**9+1
    maxS = 0
    ans = []
    for _ in range(Q):
        query = readline().split()
        if query[0] == "1":
            x = int(query[1])
            S[x] += 1
            minS = min(minS, x)
            maxS = max(maxS, x)
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            if S[x] == 0:
                continue
            if S[x] <= c:
                if x == minS:
                    minS = 10**9+1
                if x == maxS:
                    maxS = 0
            S[x] -= c
        else:
            ans.append(maxS-minS)

    print(*ans, sep="

")
