Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans = max(ans, A[i+1] - A[i])
    ans = max(ans, K - A[-1] + A[0])
    print(K - ans)

=======
Suggestion 2

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    ans = k
    for i in range(n):
        ans = min(ans, k-(a[i+1]-a[i]))
    print(ans)

=======
Suggestion 3

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if i == n-1:
            b.append(k - a[i] + a[0])
        else:
            b.append(a[i+1] - a[i])
    print(k - max(b))

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)

    ans = K
    for i in range(N):
        ans = min(ans, A[i+1] - A[i])
    print(ans)

=======
Suggestion 5

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    max = 0
    for i in range(n-1):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    if max < a[0] + k - a[n-1]:
        max = a[0] + k - a[n-1]
    print(k - max)

=======
Suggestion 6

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(d))

=======
Suggestion 7

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    diff = []
    for i in range(n):
        if i == n - 1:
            diff.append(k - a[i] + a[0])
        else:
            diff.append(a[i + 1] - a[i])
    print(k - max(diff))

=======
Suggestion 8

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_distance = 0
    for i in range(n-1):
        if max_distance < a[i+1]-a[i]:
            max_distance = a[i+1]-a[i]
    if max_distance < k - a[-1] + a[0]:
        max_distance = k - a[-1] + a[0]
    print(k-max_distance)

=======
Suggestion 9

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    ans = 10**18
    for i in range(N):
        ans = min(ans, K-(A[i+1]-A[i]))
    print(ans)
main()

=======
Suggestion 10

def main():
    # 標準入力から整数を取得する
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max = 0
    for i in range(1, n+1):
        if a[i] - a[i-1] > max:
            max = a[i] - a[i-1]
    print(k - max)
