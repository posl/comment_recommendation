Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for i in range(Q):
        L,R,X = map(int,input().split())
        print(A[L-1:R].count(X))

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        count = 0
        for i in range(L-1, R):
            if A[i] == X:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(sum([1 for a in A[L - 1:R] if a == X]))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    ans = [0]*Q
    for i in range(Q):
        L, R, X = map(int, input().split())
        for j in range(L-1, R):
            if A[j] == X:
                ans[i] += 1
    for i in range(Q):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    counter = [0] * (N+1)
    for a in A:
        counter[a] += 1
    for l, r, x in queries:
        print(counter[x])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    ans = []
    for query in queries:
        ans.append(len([i for i in A[query[0]-1:query[1]] if i==query[2]]))
    for a in ans:
        print(a)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0]*(N+1)
    for i in range(N):
        cnt[A[i]] += 1
    for i in range(Q):
        L,R,X = queries[i]
        print(cnt[X])

=======
Suggestion 10

def input(): return sys.stdin.readline().rstrip()
