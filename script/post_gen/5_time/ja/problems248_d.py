Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = [0] * Q
    R = [0] * Q
    X = [0] * Q
    for i in range(Q):
        L[i], R[i], X[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(L[i]-1, R[i]):
            if A[j] == X[i]:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def main():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    A_list = [0]*(N+1)
    for i in range(N):
        A_list[A[i]]+=1
    ans = 0
    for i in range(Q):
        L,R,X=map(int,input().split())
        ans = 0
        for j in range(L,R+1):
            if A[j-1]==X:
                ans+=1
        print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X = Query[i][2]
        print(A[L-1:R].count(X))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    ans = []
    for i in range(Q):
        ans.append(A[Query[i][0]-1:Query[i][1]].count(Query[i][2]))
    for i in range(Q):
        print(ans[i])
main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        L = Query[i][0] - 1
        R = Query[i][1] - 1
        X = Query[i][2]
        cnt = 0
        for j in range(L, R+1):
            if A[j] == X:
                cnt += 1
        print(cnt)
