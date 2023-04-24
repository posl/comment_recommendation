Synthesizing 10/10 solutions

=======
Suggestion 1

def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

=======
Suggestion 2

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort(reverse = True)
            count = 0
            for j in range(len(A)):
                if A[j] <= query[1]:
                    count += 1
                    if count == query[2]:
                        print(A[j])
                        break
            if count < query[2]:
                print(-1)
        else:
            A.sort()
            count = 0
            for j in range(len(A)):
                if A[j] >= query[1]:
                    count += 1
                    if count == query[2]:
                        print(A[j])
                        break
            if count < query[2]:
                print(-1)

=======
Suggestion 3

def main():
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            k = query[2]
            if k > len(A):
                ans.append(-1)
            else:
                ans.append(A[-k])
        elif query[0] == 3:
            A.sort()
            k = query[2]
            if k > len(A):
                ans.append(-1)
            else:
                ans.append(A[k-1])
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a <= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort(reverse=True)
                print(B[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                B.sort()
                print(B[k-1])

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        Q = list(map(int, input().split()))
        if Q[0] == 1:
            A.append(Q[1])
        elif Q[0] == 2:
            A.sort()
            if len(A) == 0:
                print(-1)
            else:
                if Q[1] < A[0]:
                    print(-1)
                else:
                    if len(A) < Q[2]:
                        print(-1)
                    else:
                        print(A[-Q[2]])
        elif Q[0] == 3:
            A.sort(reverse=True)
            if len(A) == 0:
                print(-1)
            else:
                if Q[1] > A[0]:
                    print(-1)
                else:
                    if len(A) < Q[2]:
                        print(-1)
                    else:
                        print(A[-Q[2]])

=======
Suggestion 6

def main():
    Q=int(input())
    A=[]
    for i in range(Q):
        query=input().split()
        if query[0]=='1':
            A.append(int(query[1]))
        elif query[0]=='2':
            A.sort()
            x=int(query[1])
            k=int(query[2])
            count=0
            for i in range(len(A)):
                if A[i]<=x:
                    count+=1
            if count<k:
                print(-1)
            else:
                print(A[-k])
        elif query[0]=='3':
            A.sort()
            x=int(query[1])
            k=int(query[2])
            count=0
            for i in range(len(A)):
                if A[i]>=x:
                    count+=1
            if count<k:
                print(-1)
            else:
                print(A[k-1])
main()

=======
Suggestion 7

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if query[2] > len(A):
                ans.append(-1)
            else:
                ans.append(sorted(A[:bisect_right(A, query[1])])[-query[2]])
        else:
            if query[2] > len(A):
                ans.append(-1)
            else:
                ans.append(sorted(A[bisect_left(A, query[1]):])[query[2]-1])
    print(*ans, sep='
')
main()

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    import bisect
    from collections import defaultdict
    Q = int(input())
    A = []
    D = defaultdict(list)
    ans = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x = query[1]
            bisect.insort(A,x)
            D[x].append(len(A)-1)
        elif query[0] == 2:
            x,k = query[1],query[2]
            if D[x]:
                if k <= len(D[x]):
                    ans.append(A[D[x][k-1]])
                else:
                    ans.append(-1)
            else:
                if A[0] > x:
                    ans.append(-1)
                else:
                    ans.append(A[bisect.bisect_left(A,x)-k])
        elif query[0] == 3:
            x,k = query[1],query[2]
            if D[x]:
                if k <= len(D[x]):
                    ans.append(A[D[x][-k]])
                else:
                    ans.append(-1)
            else:
                if A[-1] < x:
                    ans.append(-1)
                else:
                    ans.append(A[bisect.bisect_right(A,x)+k-1])
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    import sys
    from bisect import bisect_left, bisect_right

    Q = int(sys.stdin.readline())
    A = []
    B = []
    C = []
    for i in range(Q):
        query = sys.stdin.readline().split()
        if query[0] == '1':
            x = int(query[1])
            A.append(x)
            B.append(x)
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            C.append([x, k])
        else:
            x, k = int(query[1]), int(query[2])
            C.append([x, k])

    A.sort()
    B.sort()
    for i in range(len(C)):
        if C[i][1] == 1:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1])
        elif C[i][1] == 2:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])])
        elif C[i][1] == 3:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left(A, C[i][0]) + 1])
        elif C[i][1] == 4:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left(A, C[i][0]) + 1], A[bisect_left(A, C[i][0]) + 2])
        else:
            if C[i][0] < A[0]:
                print(-1)
            else:
                print(A[bisect_left(A, C[i][0]) - 1], A[bisect_left(A, C[i][0])], A[bisect_left

=======
Suggestion 10

def main():
    #input
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    
    #process
    #A = []
    A = set()
    ans = []
    for q in query:
        if q[0]==1:
            #A.append(q[1])
            A.add(q[1])
        elif q[0]==2:
            #A.sort()
            #A = sorted(A)
            #print(A)
            #print(A)
            #print(q[1])
            #print(q[2])
            #print(A)
            #print(len(A))
            #print(len([a for a in A if a<=q[1]]))
            #print(A)
            #print([a for a in A if a<=q[1]])
            #print([a for a in A if a<=q[1]][::-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #ans.append([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1])
            #print([a for a in A if a<=q[1]][::-1][q[2]-1] if len([a for a in A if a<=q[1]])>=q[2] else -1)
            #print([a for a in A if a<=q[1]][::-1][q
