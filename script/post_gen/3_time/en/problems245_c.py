Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        X[i] = A[i] if A[i] < B[i] else B[i]
    for i in range(N-1):
        if X[i+1] - X[i] > K:
            print('No')
            return
    print('Yes')

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if A[i] == B[i]:
            X[i] = A[i]
        else:
            X[i] = max(A[i], B[i])
    for i in range(N - 1):
        if abs(X[i] - X[i + 1]) > K:
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = []
    for i in range(N):
        if A[i] <= B[i]:
            X.append(A[i])
        else:
            if B[i] + K >= A[i]:
                X.append(B[i])
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    if n == 2:
        if abs(a[0] - a[1]) <= k or abs(b[0] - b[1]) <= k or abs(a[0] - b[1]) <= k or abs(b[0] - a[1]) <= k:
            print('Yes')
        else:
            print('No')
        return
    for i in range(1, n - 1):
        if abs(a[i] - a[i + 1]) > k and abs(a[i] - b[i + 1]) > k and abs(b[i] - a[i + 1]) > k and abs(b[i] - b[i + 1]) > k:
            print('No')
            return
    print('Yes')

main()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = []
    for i in range(N):
        if abs(A[i]-B[i]) <= K:
            X.append(min(A[i],B[i]))
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = [0]*n
    for i in range(n):
        if i == 0:
            x[i] = min(a[i],b[i])
        else:
            x[i] = min(a[i],b[i])
            if abs(x[i]-x[i-1]) > k:
                x[i] = max(a[i],b[i])
                if abs(x[i]-x[i-1]) > k:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n == 1:
        if abs(a[0] - b[0]) <= k:
            print("Yes")
            return
        else:
            print("No")
            return
    if a[0] + b[0] > k:
        print("No")
        return
    if a[-1] + b[-1] < k:
        print("No")
        return
    if a[-1] < k:
        print("Yes")
        return
    if b[-1] < k:
        print("Yes")
        return
    for i in range(n):
        if a[0] + b[-1] <= k:
            print("Yes")
            return
        if b[0] + a[-1] <= k:
            print("Yes")
            return
        if a[0] + b[-1] > k:
            if a[0] + b[-2] <= k:
                print("Yes")
                return
        if b[0] + a[-1] > k:
            if b[0] + a[-2] <= k:
                print("Yes")
                return
        a.pop(0)
        b.pop()
    print("No")
    return

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if A[0] > B[-1]:
        A,B = B,A
    if A[-1] + K < B[0]:
        print("No")
        return
    for i in range(N):
        if A[i] + K < B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # print(N, K, A, B)

    # X = [0] * N
    # X[0] = A[0]
    # X[1] = A[1]
    # X[2] = A[2]
    # X[3] = A[3]
    # X[4] = A[4]

    # print(X)

    # X[0] = A[0] or B[0]
    # X[1] = A[1] or B[1]
    # X[2] = A[2] or B[2]
    # X[3] = A[3] or B[3]
    # X[4] = A[4] or B[4]

    # X[0] = A[0] or B[0]
    # X[1] = X[0] or B[1]
    # X[2] = X[1] or B[2]
    # X[3] = X[2] or B[3]
    # X[4] = X[3] or B[4]

    # X[0] = A[0] or B[0]
    # X[1] = X[0] or B[1]
    # X[2] = X[1] or B[2]
    # X[3] = X[2] or B[3]
    # X[4] = X[3] or B[4]

    # X[0] = A[0] or B[0]
    # X[1] = X[0] or B[1]
    # X[2] = X[1] or B[2]
    # X[3] = X[2] or B[3]
    # X[4] = X[3] or B[4]

    # X[0] = A[0] or B[0]
    # X[1] = X[0] or B[1]
    # X[2] = X[1] or B[2]
    # X[3] = X[2] or B[3
