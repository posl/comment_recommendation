Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    ans = [0] * N
    cnt = 0
    for q in queries:
        if q[0] == 1:
            cnt = q[1]
        elif q[0] == 2:
            ans[q[1]-1] += q[2]
        else:
            print(A[q[1]-1] + cnt + ans[q[1]-1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    add = [0] * N
    for q in query:
        if q[0] == 1:
            add = [q[1]] * N
        elif q[0] == 2:
            add[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1] + add[q[1] - 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for q in queries:
        if q[0] == 1:
            A = [q[1]] * N
        elif q[0] == 2:
            A[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1])

=======
Suggestion 4

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #solve
    X = []
    for q in query:
        if q[0] == 1:
            a = q[1]
            A = [a] * N
        elif q[0] == 2:
            i, a = q[1], q[2]
            A[i-1] += a
        else:
            i = q[1]
            X.append(A[i-1])

    #output
    for x in X:
        print(x)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int,input().split())))
    X = []
    for q in query:
        if q[0] == 3:
            X.append(A[q[1]-1])
        elif q[0] == 1:
            A = [q[1]]*N
        else:
            A[q[1]-1] += q[2]
    for x in X:
        print(x)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    #print(a)
    #print(query)
    #print(n, q)
    #print(a)
    #print(query)
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]]*n
        if query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        if query[i][0] == 3:
            print(a[query[i][1]-1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    add = [0] * N
    assigned = [None] * N
    assigned_sum = 0

    for q in query:
        if q[0] == 1:
            assigned = [q[1]] * N
            assigned_sum = q[1] * N
        elif q[0] == 2:
            if assigned[q[1] - 1]:
                assigned[q[1] - 1] += q[2]
                assigned_sum += q[2]
            else:
                add[q[1] - 1] += q[2]
        else:
            if assigned[q[1] - 1]:
                print(assigned[q[1] - 1])
            else:
                print(A[q[1] - 1] + add[q[1] - 1] + assigned_sum)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    d = {}
    for q in range(Q):
        if query[q][0] == "1":
            d = {}
            d[int(query[q][1])] = N
        elif query[q][0] == "2":
            if int(query[q][2]) in d:
                d[int(query[q][2])] += 1
            else:
                d[int(query[q][2])] = 1
        else:
            if int(query[q][1]) in d:
                print(A[int(query[q][1]) - 1] + d[int(query[q][1])])
            else:
                print(A[int(query[q][1]) - 1])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(str, input().split())) for _ in range(Q)]

    # 1, 2, 3のクエリをそれぞれ分けて保持する
    queries_1 = []
    queries_2 = []
    queries_3 = []
    for query in queries:
        if query[0] == "1":
            queries_1.append(query)
        elif query[0] == "2":
            queries_2.append(query)
        else:
            queries_3.append(query)

    # 1のクエリを処理する
    for query in queries_1:
        A = [int(query[1])] * N

    # 2のクエリを処理する
    for query in queries_2:
        A[int(query[1]) - 1] += int(query[2])

    # 3のクエリを処理する
    for query in queries_3:
        print(A[int(query[1]) - 1])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    # 1. 0, 1, 2, 3, ... というインデックスをもつ配列を作る
    # 2. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 3. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 4. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 5. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 6. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 7. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 8. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 9. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 10. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 11. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 12. 1の配列の各要素に対して、その要素を含む配列の和を計算する
    # 13. 1の配列の各要素に対して、その要素を含む
