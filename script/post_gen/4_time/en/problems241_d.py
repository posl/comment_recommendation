Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[-query[2]])
        else:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])

=======
Suggestion 2

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            cnt = 0
            for i in range(len(A)):
                if A[i] <= query[1]:
                    cnt += 1
                    if cnt == query[2]:
                        print(A[i])
                        break
            if cnt < query[2]:
                print(-1)
        else:
            A.sort(reverse=True)
            cnt = 0
            for i in range(len(A)):
                if A[i] >= query[1]:
                    cnt += 1
                    if cnt == query[2]:
                        print(A[i])
                        break
            if cnt < query[2]:
                print(-1)

=======
Suggestion 3

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            A = sorted(A)
            x = int(query[1])
            k = int(query[2])
            if k > len(A):
                print(-1)
            else:
                cnt = 0
                for j in range(len(A)):
                    if A[j] <= x:
                        cnt += 1
                        if cnt == k:
                            print(A[j])
                            break
        elif query[0] == '3':
            A = sorted(A,reverse=True)
            x = int(query[1])
            k = int(query[2])
            if k > len(A):
                print(-1)
            else:
                cnt = 0
                for j in range(len(A)):
                    if A[j] >= x:
                        cnt += 1
                        if cnt == k:
                            print(A[j])
                            break

=======
Suggestion 4

def main():
    import bisect
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            bisect.insort(A,query[1])
        elif query[0] == 2:
            id = bisect.bisect_right(A,query[1])
            if id < query[2]:
                ans.append(-1)
            else:
                ans.append(A[id-query[2]])
        elif query[0] == 3:
            id = bisect.bisect_left(A,query[1])
            if len(A)-id < query[2]:
                ans.append(-1)
            else:
                ans.append(A[id+query[2]-1])
    for i in ans:
        print(i)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
            b.append(int(s[1]))
        elif s[0] == '2':
            a.sort()
            k = int(s[2])
            if len(a) < k:
                print(-1)
            else:
                print(a[-k])
        elif s[0] == '3':
            b.sort()
            k = int(s[2])
            if len(b) < k:
                print(-1)
            else:
                print(b[k-1])
    return

main()

=======
Suggestion 6

def main():
    import bisect
    import sys
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bisect.insort(A, query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                ans.append(-1)
            else:
                ans.append(A[-query[2]])
        elif query[0] == 3:
            if len(A) < query[2]:
                ans.append(-1)
            else:
                ans.append(A[query[2]-1])
    for i in ans:
        print(i)
    return 0

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    Q = int(input())
    A = []
    D = defaultdict(list)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]].append(i)
        elif query[0] == 2:
            x, k = query[1], query[2]
            if len(A) < k:
                print(-1)
            else:
                idx = bisect_right(A, x)
                if idx < k:
                    print(-1)
                else:
                    print(A[idx-k])
        else:
            x, k = query[1], query[2]
            if len(A) < k:
                print(-1)
            else:
                idx = bisect_left(A, x)
                if len(A)-idx < k:
                    print(-1)
                else:
                    print(A[idx+k-1])
main()

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline

    Q = int(input())
    A = []
    for _ in range(Q):
        query = input().rstrip().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            A.sort(reverse=True)
            count = 0
            for a in A:
                if a <= x:
                    count += 1
                    if count == k:
                        print(a)
                        break
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            A.sort()
            count = 0
            for a in A:
                if a >= x:
                    count += 1
                    if count == k:
                        print(a)
                        break
            else:
                print(-1)

=======
Suggestion 10

def main():
    import sys
    import bisect
    input = sys.stdin.readline
    Q = int(input())
    A = []
    B = []
    C = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            bisect.insort(A,query[1])
            bisect.insort(B,query[1])
            bisect.insort(C,query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[-query[2]])
                bisect.insort(B,A[-query[2]])
                bisect.insort(C,A[-query[2]])
                A.pop(-query[2])
        else:
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])
                bisect.insort(A,B[query[2]-1])
                bisect.insort(C,B[query[2]-1])
                B.pop(query[2]-1)
    return
