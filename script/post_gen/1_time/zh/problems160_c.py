Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    ans = K
    for i in range(N):
        ans = min(ans, K - (A[i + 1] - A[i]))
    print(ans)

=======
Suggestion 2

def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算距离
    A.append(K)
    A.append(K + A[0])
    A.sort()
    # print(A)
    dist = [A[i] - A[i - 1] for i in range(1, N + 2)]
    # print(dist)
    print(K - max(dist))

=======
Suggestion 3

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K+A[0])
    max = 0
    for i in range(N):
        if A[i+1] - A[i] > max:
            max = A[i+1] - A[i]
    print(K - max)

=======
Suggestion 4

def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算最短距离
    max_len = 0
    for i in range(N):
        if i == N - 1:
            max_len = max(max_len, K - A[i] + A[0])
        else:
            max_len = max(max_len, A[i + 1] - A[i])
    print(K - max_len)

=======
Suggestion 5

def solve(K, N, A):
    A.append(K)
    A.sort()
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + 1] - A[i])
    return K - ans
K, N = map(int, input().split())
A = list(map(int, input().split()))
print(solve(K, N, A))

=======
Suggestion 6

def solve(k, n, a):
    a.sort()
    a.append(a[0] + k)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 1] - a[i])
    return k - ans

k, n = map(int, input().split())
a = list(map(int, input().split()))
print(solve(k, n, a))

=======
Suggestion 7

def main():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(A[0]+K)
    distance = []
    for i in range(N):
        distance.append(A[i+1]-A[i])
    print(K-max(distance))

=======
Suggestion 8

def solve(k, n, a):
    ans = k
    for i in range(n - 1):
        ans = min(ans, k - abs(a[i + 1] - a[i]))
    return ans

=======
Suggestion 9

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(a[0]+k)
    d = [a[i+1]-a[i] for i in range(n)]
    print(k-max(d))

=======
Suggestion 10

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    max = 0
    for i in range(N):
        if i == N-1:
            if max < K - A[i] + A[0]:
                max = K - A[i] + A[0]
        else:
            if max < A[i+1] - A[i]:
                max = A[i+1] - A[i]

    print(K-max)
