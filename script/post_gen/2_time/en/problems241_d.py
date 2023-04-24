Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    for _ in range(N):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            B = [a for a in A if a <= q[1]]
            if len(B) >= q[2]:
                print(sorted(B, reverse=True)[q[2]-1])
            else:
                print(-1)
        elif q[0] == 3:
            B = [a for a in A if a >= q[1]]
            if len(B) >= q[2]:
                print(sorted(B)[q[2]-1])
            else:
                print(-1)

=======
Suggestion 2

def main():
    import bisect
    Q=int(input())
    A=[]
    ans=[]
    for i in range(Q):
        query=list(map(int,input().split()))
        if query[0]==1:
            bisect.insort(A,query[1])
        elif query[0]==2:
            if len(A)<query[2]:
                ans.append(-1)
            else:
                ans.append(A[-query[2]])
        else:
            if len(A)<query[2]:
                ans.append(-1)
            else:
                ans.append(A[query[2]-1])
    print('\n'.join(map(str,ans)))
main()

=======
Suggestion 3

def main():
    Q=int(input())
    A=[]
    for i in range(Q):
        query=input().split()
        c=int(query[0])
        if c==1:
            A.append(int(query[1]))
        elif c==2:
            x=int(query[1])
            k=int(query[2])
            A=list(filter(lambda a:a<=x,A))
            A.sort(reverse=True)
            if len(A)>=k:
                print(A[k-1])
            else:
                print(-1)
        elif c==3:
            x=int(query[1])
            k=int(query[2])
            A=list(filter(lambda a:a>=x,A))
            A.sort()
            if len(A)>=k:
                print(A[k-1])
            else:
                print(-1)

=======
Suggestion 4

def bisect_left(a, x, lo=0, hi=None): # find leftmost value greater than or equal to x
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

=======
Suggestion 5

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for i in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            k = bisect_right(A, q[1])
            if k >= q[2]:
                print(sorted(A[:k])[-q[2]])
            else:
                print(-1)
        else:
            k = bisect_left(A, q[1])
            if len(A) - k >= q[2]:
                print(sorted(A[k:])[q[2]-1])
            else:
                print(-1)
    return

=======
Suggestion 6

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    N = int(input())
    A = []
    for _ in range(N):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A.append(q[1])
        elif q[0] == 2:
            k = bisect_right(A, q[1])
            if k >= q[2]:
                print(sorted(A[:k])[-q[2]])
            else:
                print(-1)
        else:
            k = bisect_left(A, q[1])
            if len(A) - k >= q[2]:
                print(sorted(A[k:])[-q[2]])
            else:
                print(-1)
    return

=======
Suggestion 7

def main():
    Q = int(input())
    A = []
    A2 = []
    for i in range(Q):
        c = list(map(int, input().split()))
        if c[0] == 1:
            A.append(c[1])
            A2.append(c[1])
        elif c[0] == 2:
            A = sorted(A, reverse=True)
            if len(A) < c[2]:
                print(-1)
            else:
                print(A[c[2]-1])
        elif c[0] == 3:
            A2 = sorted(A2)
            if len(A2) < c[2]:
                print(-1)
            else:
                print(A2[c[2]-1])

=======
Suggestion 8

def main():
    from bisect import bisect_left, bisect_right
    from collections import defaultdict

    Q = int(input())
    A = []
    D = defaultdict(list)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]].append(_)
        elif query[0] == 2:
            i = bisect_right(A, query[1])
            if i < query[2]:
                print(-1)
            else:
                print(A[i - query[2]])
        else:
            i = bisect_left(A, query[1])
            if len(A) - i < query[2]:
                print(-1)
            else:
                print(A[i + query[2] - 1])

=======
Suggestion 9

def main():
    from bisect import bisect_left,bisect_right
    from heapq import heappop,heappush
    Q=int(input())
    A=[]
    for _ in range(Q):
        c,x,k=map(int,input().split())
        if c==1:
            bisect.insort(A,x)
        elif c==2:
            ans=-1
            if len(A)>=k:
                ans=A[-k]
            print(ans)
        else:
            ans=-1
            if len(A)>=k:
                ans=A[k-1]
            print(ans)
    return

=======
Suggestion 10

def main():
    import sys
    from bisect import bisect_left
    from collections import deque

    q = int(sys.stdin.readline())
    a = deque()
    for _ in range(q):
        c, x, k = map(int, sys.stdin.readline().split())
        if c == 1:
            a.append(x)
        else:
            a.sort()
            if c == 2:
                ind = bisect_left(a, x)
                if ind >= len(a):
                    print(-1)
                else:
                    print(a[ind])
            else:
                ind = bisect_left(a, x)
                if ind == 0:
                    print(-1)
                else:
                    print(a[ind - 1])
