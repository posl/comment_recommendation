Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    #print(N, Q)
    #print(A)
    #print(X)
    #print(K)
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] == X[i]:
                count += 1
            if count == K[i]:
                print(j+1)
                break
        else:
            print(-1)

main()

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())

    # A = [1, 1, 2, 3, 1, 2]
    # X = [1, 1, 1, 1, 2, 2, 2, 4]
    # K = [1, 2, 3, 4, 1, 2, 3, 1]

    # A = [0, 1000000000, 999999999]
    # X = [1000000000, 123456789]
    # K = [1, 1]

    # A = [1, 1, 1, 1, 2, 2, 2, 4]
    # X = [1, 1, 1, 1, 2, 2, 2, 4]
    # K = [1, 2, 3, 4, 1, 2, 3, 1]

    # A = [1, 1, 1, 1, 2, 2, 2, 4]
    # X = [1, 1, 1, 1, 2, 2, 2, 4]
    # K = [1, 2, 3, 4, 1, 2, 3, 1]

    # A = [1, 1, 1, 1, 2, 2, 2, 4]
    # X = [1, 1, 1, 1, 2, 2, 2, 4]
    # K = [1, 2, 3, 4, 1, 2, 3, 1]

    # A = [1, 1, 1, 1, 2, 2, 2, 4]
    # X = [1, 1, 1, 1, 2, 2, 2, 4]
    # K = [1

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())

    # dictionary of lists
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i)
        else:
            d[A[i]] = [i]

    for i in range(Q):
        if X[i] in d and len(d[X[i]]) >= K[i]:
            print(d[X[i]][K[i] - 1] + 1)
        else:
            print(-1)

=======
Suggestion 4

def main():
    N, Q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    for q in range(Q):
        x, k = [int(i) for i in input().split()]
        count = 0
        for i in range(N):
            if A[i] == x:
                count += 1
            if count == k:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*Q
    K = [0]*Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    ans = [0]*Q
    for i in range(N):
        for j in range(Q):
            if A[i] == X[j]:
                K[j] -= 1
                if K[j] == 0:
                    ans[j] = i+1
    for i in range(Q):
        if ans[i] == 0:
            ans[i] = -1
    for i in range(Q):
        print(ans[i])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i] = A[i]
        Y[i] = i + 1
    for _ in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(N):
            if X[i] == x:
                cnt += 1
                if cnt == k:
                    print(Y[i])
                    break
        else:
            print(-1)

=======
Suggestion 7

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(q):
        x,k = map(int,input().split())
        c = 0
        for j in range(n):
            if a[j] == x:
                c += 1
            if c == k:
                ans.append(j+1)
                break
        else:
            ans.append(-1)
    print('

'.join(map(str,ans)))

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]

    # indexをキーにして、その数値が何番目かを保存する辞書
    # 例：{1: [0, 4], 2: [2, 5], 3: [3]}
    dic = {}
    for i, v in enumerate(a):
        if v in dic:
            dic[v].append(i)
        else:
            dic[v] = [i]

    for x, k in queries:
        if x in dic and len(dic[x]) >= k:
            print(dic[x][k - 1] + 1)
        else:
            print(-1)

=======
Suggestion 9

def search(lst, x, k):
    #print("lst",lst)
    #print("x",x)
    #print("k",k)
    if x not in lst:
        return -1
    else:
        if k > lst.count(x):
            return -1
        else:
            return lst.index(x) + 1

N, Q = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(Q):
    x, k = map(int, input().split())
    print(search(A, x, k))

=======
Suggestion 10

def process_queries(queries, numbers):
    #print(queries)
    #print(numbers)
    result = []
    for query in queries:
        #print(query)
        #print(numbers)
        #print(result)
        x = query[0]
        k = query[1]
        if k > len(numbers):
            result.append(-1)
        else:
            if x in numbers:
                if k <= numbers[x]:
                    result.append(numbers[x][k-1])
                else:
                    result.append(-1)
            else:
                result.append(-1)
    return result
