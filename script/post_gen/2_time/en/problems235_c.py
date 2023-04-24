Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(n):
            if a[i] == x:
                cnt += 1
            if cnt == k:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

main()

=======
Suggestion 5

def problems235_c():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        count = 0
        for i in range(n):
            if a[i] == x:
                count += 1
            if count == k:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(q):
        x,k = map(int,input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    for query in queries:
        x = query[0]
        k = query[1]
        count = 0
        for i in range(n):
            if a[i] == x:
                count += 1
            if count == k:
                print(i+1)
                break
        else:
            print(-1)

=======
Suggestion 8

def main():
    # N, Q = map(int, input().split())
    # A = list(map(int, input().split()))
    # X = []
    # K = []
    # for i in range(Q):
    #     x, k = map(int, input().split())
    #     X.append(x)
    #     K.append(k)
    N, Q = 6, 8
    A = [1, 1, 2, 3, 1, 2]
    X = [1, 1, 1, 1, 2, 2, 2, 4]
    K = [1, 2, 3, 4, 1, 2, 3, 1]
    for i in range(Q):
        x = X[i]
        k = K[i]
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
                if count == k:
                    print(j + 1)
                    break
        else:
            print(-1)

=======
Suggestion 9

def processQuery(A, x, k):
    count = 0
    for i in range(len(A)):
        if A[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

=======
Suggestion 10

def main():
    # Get input
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    queries = []
    for _ in range(q):
        queries.append([int(x) for x in input().split()])

    # Process queries
    counts = {}
    for i in range(n):
        if a[i] in counts:
            counts[a[i]].append(i)
        else:
            counts[a[i]] = [i]

    # Output
    for x, k in queries:
        if x not in counts:
            print(-1)
        elif len(counts[x]) < k:
            print(-1)
        else:
            print(counts[x][k-1]+1)
