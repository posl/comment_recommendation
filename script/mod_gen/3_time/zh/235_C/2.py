def find(x, k):
    cnt = 0
    for i in range(len(A)):
        if A[i] == x:
            cnt += 1
            if cnt == k:
                return i + 1
    return -1
N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = []
K = []
for i in range(Q):
    x, k = map(int, input().split())
    X.append(x)
    K.append(k)
for i in range(Q):
    print(find(X[i], K[i]))
