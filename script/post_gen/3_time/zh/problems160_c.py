Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K)
    A.append(K+A[1])
    A.sort()
    min = K
    for i in range(N):
        if A[i+1] - A[i] < min:
            min = A[i+1] - A[i]
    print(min)

=======
Suggestion 2

def solve():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(A[0]+K)
    m = 0
    for i in range(N):
        m = max(m,A[i+1]-A[i])
    print(K-m)
solve()

=======
Suggestion 3

def main():
    # 读入数据
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    # 计算最短距离
    min_dist = k
    for i in range(n):
        dist = k - a[i]
        if i == n - 1:
            dist += a[0]
        else:
            dist += a[i + 1]
        if dist < min_dist:
            min_dist = dist

    # 打印结果
    print(min_dist)

=======
Suggestion 4

def min_distance(k, n, a):
    distance = 0
    for i in range(n-1):
        distance += min(abs(a[i+1]-a[i]), k-abs(a[i+1]-a[i]))
    return distance

=======
Suggestion 5

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    ans = k
    for i in range(n):
        ans = min(ans, k - (a[i+1] - a[i]))
    print(ans)

=======
Suggestion 6

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k+a[0])
    ans = k
    for i in range(n):
        ans = min(ans,a[i+1]-a[i])
    print(ans)

=======
Suggestion 7

def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    ans = K
    for i in range(N):
        if i == 0:
            ans = min(ans, K - A[N - 1] + A[1] - A[0])
        elif i == N - 1:
            ans = min(ans, K - A[N - 2] + A[N - 1] - A[0])
        else:
            ans = min(ans, K - A[i - 1] + A[i + 1] - A[i])

    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算最大距离
    max_dist = 0
    for i in range(N):
        if i == N - 1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i + 1] - A[i]
        if dist > max_dist:
            max_dist = dist
    # 计算答案
    print(K - max_dist)
main()

=======
Suggestion 9

def solve(K, N, A):
    A.sort()
    ret = K
    for i in range(N):
        if i == N-1:
            ret = min(ret, K-A[i]+A[0])
        else:
            ret = min(ret, A[i+1]-A[i])
    return ret

=======
Suggestion 10

def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # output
    print(min(K-A[-1]+A[0], A[-1]-A[0]))
main()
