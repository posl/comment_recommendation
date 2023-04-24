Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(x) for x in input().split()])
    A = [0] + A
    for i in range(1, N+1):
        A[i] = A[i-1] + A[i]
    for query in queries:
        L, R, X = query
        print(A[R] - A[L-1] - (R - L + 1) * X)

=======
Suggestion 5

def main():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  for _ in range(q):
    l, r, x = map(int, input().split())
    print(sum(1 for i in range(l-1, r) if a[i] == x))
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    counter = [0] * N
    for a in A:
        counter[a - 1] += 1
    for l, r, x in queries:
        print(counter[x - 1] - (A[l - 1] != x) - (A[r - 1] != x))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N)
    #print(A)
    #print(Q)
    #print(query)
    
    #Aの要素をインデックスにしたリストを作成
    #Aの要素をインデックスにしたリストの要素をインデックスにしたリストを作成
    #Aの要素をインデックスにしたリストの要素をインデックスにしたリストの要素をインデックスにしたリストを作成
    #Aの要素をインデックスにしたリストの要素をインデックスにしたリストの要素をインデックスにしたリストの要素をインデックスにしたリストを作成
    #A

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    # Aの要素をindexに、Aの要素の出現回数をvalueにした辞書を作成
    A_dict = {}
    for i in range(N):
        if A[i] in A_dict:
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1

    # Q個のクエリについて、Aの要素の出現回数を出力
    for i in range(Q):
        L, R, X = map(int, input().split())
        if X in A_dict:
            print(A_dict[X])
        else:
            print(0)
