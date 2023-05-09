def main():
    from bisect import bisect_left
    from bisect import bisect_right
    from collections import defaultdict
    from collections import deque
    import heapq
    import math
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    Q = int(input())
    A = []
    for _ in range(Q):
        c,x,k = map(int,input().split())
        if c==1:
            A.append(x)
        else:
            if c==2:
                A.sort()
                #print(A)
                k = min(k,len(A))
                if k==0:
                    print(-1)
                else:
                    print(A[-k])
            if c==3:
                A.sort()
                k = min(k,len(A))
                if k==0:
                    print(-1)
                else:
                    print(A[k-1])
