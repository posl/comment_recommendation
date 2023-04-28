Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    for i in range(Q):
        L, R, X = Query[i][0], Query[i][1], Query[i][2]
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(x) for x in input().split()])
    
    #print(N)
    #print(A)
    #print(Q)
    #print(queries)
    
    for i in range(Q):
        L = queries[i][0]
        R = queries[i][1]
        X = queries[i][2]
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    for i in range(q):
        print(a[query[i][0]-1:query[i][1]].count(query[i][2]))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    
    for i in range(Q):
        count = 0
        for j in range(query[i][0]-1, query[i][1]):
            if A[j] == query[i][2]:
                count += 1
        print(count)

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from collections import defaultdict

    N = int(readline())
    A = list(map(int,readline().split()))
    Q = int(readline())
    Query = [list(map(int,readline().split())) for i in range(Q)]

    ans = [0]*Q
    for i in range(Q):
        L,R,X = Query[i]
        ans[i] = A[L-1:R].count(X)

    print(*ans,sep='\n')

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #print(N)
    #print(A)
    #print(Q)
    #print(query)

    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        X = query[i][2]

        #print(L, R, X)
        #print(A[L-1:R].count(X))

        print(A[L-1:R].count(X))

main()
