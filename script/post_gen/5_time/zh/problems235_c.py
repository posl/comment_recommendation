Synthesizing 10/10 solutions (Duplicates hidden)

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
                print(j + 1)
                break
        else:
            print(-1)

=======
Suggestion 2

def find_kth(a, x, k):
    count = 1
    for i in range(len(a)):
        if a[i] == x:
            if count == k:
                return i+1
            count += 1
    return -1

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
                if cnt == k:
                    print(j + 1)
                    break
        else:
            print(-1)

=======
Suggestion 4

def get_index(arr, x, k):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i + 1
    return -1

=======
Suggestion 5

def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    return N, Q, A, X, K

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        if x not in A:
            print(-1)
        else:
            print(A.index(x, k-1)+1)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        index = 0
        count = 0
        for j in range(N):
            if a[j] == x:
                count += 1
            if count == k:
                index = j + 1
                break
        if index == 0:
            print(-1)
        else:
            print(index)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

main()

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
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
