Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))

    # 处理
    for i in range(Q):
        L, R, X = Query[i][0], Query[i][1], Query[i][2]
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for i in range(Q):
        L,R,X = map(int,input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def solve(n, a, q, query):
    ans = []
    for l, r, x in query:
        ans.append(a[l - 1:r].count(x))
    return ans

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        l, r, x = map(int, input().split())
        queries.append((l, r, x))
    for query in queries:
        l, r, x = query
        print(a[l-1:r].count(x))

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    for i in range(q):
        l, r, x = [int(x) for x in input().split()]
        print(a[l-1:r].count(x))

=======
Suggestion 6

def find_num(A,L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count

=======
Suggestion 7

def count(L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

for i in range(Q):
    L,R,X = map(int,input().split())
    print(count(L,R,X))

=======
Suggestion 8

def count_element(A, L, R, X):
    count = 0
    for i in range(L-1, R):
        if A[i] == X:
            count += 1
    return count

=======
Suggestion 9

def countx(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count

N = int(input())
A = list(map(int, input().split()))

Q = int(input())
Query = []
for i in range(Q):
    Query.append(list(map(int, input().split())))

for i in range(Q):
    print(countx(A[Query[i][0]-1:Query[i][1]], Query[i][2]))

=======
Suggestion 10

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        l, r, x = [int(i) for i in input().split()]
        print(a[l-1:r].count(x))
