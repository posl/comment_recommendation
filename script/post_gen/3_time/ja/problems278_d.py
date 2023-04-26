Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    n = int(readline())
    a = list(map(int,readline().split()))
    q = int(readline())
    ans = sum(a)
    for _ in range(q):
        t,*query = map(int,readline().split())
        if t == 1:
            x = query[0]
            ans += n * x
        elif t == 2:
            i,x = query
            ans += x
        else:
            i = query[0]
            print(a[i - 1] + ans)
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    for i in range(Q):
        if query[i][0] == 1:
            A = [query[i][1]]*N
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            for j in range(n):
                a[j] = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        else:
            ans.append(a[query[i][1]-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int, input().split())))
    
    ans = sum(A)
    for q in query:
        if q[0] == 1:
            ans += (N * q[1])
        elif q[0] == 2:
            ans += q[1] * A[q[1] - 1]
            A[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        if query[i][0] == 1:
            sum += (query[i][1] - A[query[i][1]-1])
            A[query[i][1]-1] = query[i][1]
        elif query[i][0] == 2:
            sum += query[i][2]
            A[query[i][1]-1] += query[i][2]
        else:
            print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, queries)

    #A = [3, 1, 4, 1, 5]
    #queries = [[3, 2], [

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    sumA = sum(A)
    for query in queries:
        if query[0] == 1:
            sumA = sumA - N*query[1]
        elif query[0] == 2:
            sumA = sumA + query[1]*A[query[2]-1]
            A[query[2]-1] = A[query[2]-1] + query[1]
        else:
            print(A[query[1]-1])

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    query3s = [q for q in queries if q[0] == 3]
    query3s.sort(key=lambda x: x[1])
    query3s = [q[1] for q in query3s]
    query3s = list(set(query3s))
    query3s.sort()
    query3s = [q-1 for q in query3s]
    #print(query3s)
    query3s.reverse()
    query3s = set(query3s)
    #print(query3s)
    A = [0] + A
    #print(A)
    for q in queries:
        if q[0] == 1:
            A = [q[1]] * (N+1)
        elif q[0] == 2:
            A[q[1]] += q[2]
        elif q[0] == 3:
            if q[1] in query3s:
                print(A[q[1]])
                query3s.remove(q[1])
    return

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    query1 = [i for i in query if i[0] == 1]
    query2 = [i for i in query if i[0] == 2]
    query3 = [i for i in query if i[0] == 3]
    #print(query1)
    #print(query2)
    #print(query3)
    for i in query1:
        a = [i[1] for _ in range(n)]
    #print(a)
    for i in query2:
        a[i[1]-1] += i[2]
    #print(a)
    for i in query3:
        print(a[i[1]-1])

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    # 1-indexed
    bit = [0] * (n+1)

    def add(i, x):
        while i <= n:
            bit[i] += x
            i += i & (-i)

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & (-i)
        return res

    for i, x in enumerate(a):
        add(i+1, x)

    for query_type, *query_value in query:
        if query_type == 1:
            x = query_value[0]
            for i in range(1, n+1):
                add(i, x)
        elif query_type == 2:
            i, x = query_value
            add(i, x)
        else:
            i = query_value[0]
            print(sum(i))
