Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L - 1:R].count(X))

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        L, R, X = query
        print(A[L-1:R].count(X))

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    Q = int(input())
    query = []
    for _ in range(Q):
        L, R, X = [int(a) for a in input().split()]
        query.append((L, R, X))

    # 1. 1-indexedにする
    # 2. 1-indexedにしたAを、A[i]を値とする要素の数を数える
    A = [0] + A
    count = [0] * (N + 1)
    for a in A:
        count[a] += 1

    # 3. 累積和を取る
    cumsum = [0] * (N + 1)
    for i in range(1, N + 1):
        cumsum[i] = cumsum[i - 1] + count[i]

    # 4. 累積和を用いて、各クエリに対する解を出力する
    for L, R, X in query:
        print(cumsum[R] - cumsum[L - 1])

=======
Suggestion 5

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Qs = []
    for _ in range(Q):
        L, R, X = map(int, input().split())
        Qs.append((L, R, X))
    return N, A, Q, Qs

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    #print(N, A, Q, queries)
    
    # 1. count the number of each number
    count = [0] * (N+1)
    for a in A:
        count[a] += 1
    
    # 2. accumulative sum
    accum = [0] * (N+1)
    for i in range(1, N+1):
        accum[i] = accum[i-1] + count[i]
    
    # 3. answer queries
    for l, r, x in queries:
        print(accum[r] - accum[l-1])

solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L_R_X = [list(map(int, input().split())) for _ in range(Q)]
    for l, r, x in L_R_X:
        print(A[l-1:r].count(x))

=======
Suggestion 8

def solve():
    from collections import Counter
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for _ in range(Q):
        L, R, X = [int(x) for x in input().split()]
        queries.append((L, R, X))
    count = Counter(A)
    ans = []
    for L, R, X in queries:
        ans.append(count[X])
    print(*ans, sep='

')

solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #Aの値に対応するindexを格納
    index = [[] for _ in range(N)]
    for i, a in enumerate(A):
        index[a-1].append(i)

    for l, r, x in query:
        #indexは0番目から始まるのでl-1,r-1
        print(len([i for i in index[x-1] if l-1 <= i <= r-1]))

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    #Aの要素の値をキーに、その要素のインデックスを値とする辞書を作成
    #例えば、A = [3,1,4,1,5]の場合、
    #A_dict = {3:0, 1:1, 4:2, 5:4}となる
    A_dict = {A[i]:i for i in range(N)}
    Q_list = []
    for i in range(Q):
        Q_list.append([int(x) for x in input().split()])
    #Q_list[i] = [L,R,X]
    #L,Rはインデックスで表されるので、実際の要素の値を取得するためには、
    #L-1,R-1とする
    for i in range(Q):
        L = Q_list[i][0]-1
        R = Q_list[i][1]-1
        X = Q_list[i][2]
        #XがAの要素の値として存在するかどうかをチェック
        if X in A_dict:
            #存在する場合、Xのインデックスを取得
            X_index = A_dict[X]
            #L以上R以下のインデックスにX_indexが含まれるかどうかをチェック
            if L <= X_index <= R:
                #含まれる場合、Xを含む要素の個数はR-L+1
                print(R-L+1)
            else:
                #含まれない場合、Xを含む要素の個数はR-L
                print(R-L)
        else:
            #存在しない場合、Xを含む要素の個数は0
            print(0)
