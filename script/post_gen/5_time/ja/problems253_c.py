Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    q = int(input())
    s = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
        elif query[0] == 2:
            for i in range(query[1]):
                if query[1] == 0:
                    break
                if s.count(query[1]) >= query[2]:
                    s.remove(query[1])
        else:
            print(max(s) - min(s))

=======
Suggestion 2

def main():
    from sys import stdin
    from collections import Counter
    readline = stdin.readline

    q = int(readline())
    A = []
    for _ in range(q):
        query = list(map(int,readline().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) > 0:
                cnt = Counter(A)
                for i in range(min(query[2],cnt[query[1]])):
                    A.remove(query[1])
        else:
            A.sort()
            print(A[-1] - A[0])

=======
Suggestion 3

def main():
    from sys import stdin
    input = stdin.readline
    
    from heapq import heappush, heappop
    
    Q = int(input())
    s = []
    h = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1])
            s.append(x)
            heappush(h, x)
        elif query[0] == "2":
            x = int(query[1])
            c = int(query[2])
            for i in range(min(c, s.count(x))):
                s.remove(x)
        else:
            while True:
                if s[0] == h[0]:
                    heappop(h)
                    heappop(s)
                else:
                    break
            print(h[0]-s[0])

=======
Suggestion 4

def main():
    #n = int(input())
    #a, b = list(map(int, input().split()))
    #s = input()
    #s = input().split()
    q = int(input())
    #query = [list(map(int, input().split())) for i in range(q)]
    query = [input().split() for i in range(q)]
    #print(query)
    #print(query[0][0])
    s = []
    for i in range(q):
        if query[i][0] == "1":
            s.append(int(query[i][1]))
        elif query[i][0] == "2":
            num = int(query[i][1])
            count = int(query[i][2])
            for j in range(count):
                if num in s:
                    s.remove(num)
                else:
                    break
        else:
            s.sort()
            print(s[-1] - s[0])
    #print(s)

=======
Suggestion 5

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    S = Counter()
    S_max = 0
    S_min = 0
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            S[query[1]] += 1
            if S_max == 0:
                S_max = query[1]
                S_min = query[1]
            else:
                if S_max < query[1]:
                    S_max = query[1]
                if S_min > query[1]:
                    S_min = query[1]
        elif query[0] == 2:
            if S[query[1]] > 0:
                if S[query[1]] - query[2] > 0:
                    S[query[1]] -= query[2]
                else:
                    S[query[1]] = 0
        elif query[0] == 3:
            print(S_max - S_min)
        else:
            pass

=======
Suggestion 6

def main():
    from sys import stdin
    from collections import Counter
    read=stdin.readline
    N=int(read())
    S=Counter()
    S_max=0
    S_min=10**9
    for i in range(N):
        query=read().split()
        if query[0]=='1':
            S[int(query[1])]+=1
            S_max=max(S_max,int(query[1]))
            S_min=min(S_min,int(query[1]))
        elif query[0]=='2':
            if S[int(query[1])]>0:
                if S[int(query[1])]<int(query[2]):
                    S_min=max(S_min,int(query[1]))
                    S[int(query[1])]-=S[int(query[1])]
                else:
                    S[int(query[1])]-=int(query[2])
        else:
            print(S_max-S_min)

=======
Suggestion 7

def main():
  import sys
  def input(): return sys.stdin.readline().rstrip()
  from collections import defaultdict
  from heapq import heappush, heappop

  q = int(input())
  s = []
  d = defaultdict(int)
  for _ in range(q):
    query = input().split()
    if query[0] == '1':
      heappush(s, int(query[1]))
      d[int(query[1])] += 1
    elif query[0] == '2':
      while s and d[s[0]] == 0:
        heappop(s)
      if s:
        d[heappop(s)] -= 1
    else:
      while s and d[s[0]] == 0:
        heappop(s)
      print(s[-1] - s[0])
  return

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    from heapq import heapify, heappop, heappush
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    S = []
    S_cnt = Counter()
    S_min = 10**9+1
    S_max = -1
    for q in query:
        if q[0] == "1":
            x = int(q[1])
            S.append(x)
            S_cnt[x] += 1
            S_min = min(S_min, x)
            S_max = max(S_max, x)
        elif q[0] == "2":
            x = int(q[1])
            c = int(q[2])
            while c > 0:
                if S_cnt[x] > 0:
                    S_cnt[x] -= 1
                    S.remove(x)
                    c -= 1
                else:
                    break
            if S_cnt[x] == 0:
                S_min = min(S)
                S_max = max(S)
        else:
            print(S_max - S_min)
main()

=======
Suggestion 9

def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.buffer.readline
    q = int(input())
    add = []
    dels = []
    c = Counter()
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            add.append(query[1])
        elif query[0] == 2:
            dels.append(query[1])
            c[query[1]] += 1
        else:
            while add:
                if c[add[-1]] > 0:
                    c[add[-1]] -= 1
                    add.pop()
                else:
                    break
            while dels:
                if c[dels[-1]] == 0:
                    dels.pop()
                else:
                    break
            print(add[-1] - dels[-1])

=======
Suggestion 10

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    S = []
    for i in range(Q):
        if query[i][0] == 1:
            S.append(query[i][1])
        elif query[i][0] == 2:
            for j in range(min(query[i][2], S.count(query[i][1]))):
                S.remove(query[i][1])
        elif query[i][0] == 3:
            print(max(S) - min(S))
