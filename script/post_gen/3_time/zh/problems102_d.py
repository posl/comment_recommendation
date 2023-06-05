Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    a = [0] + a
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    ans = 10 ** 18
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = a[i]
            y = a[j] - a[i]
            z = a[n] - a[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    l = 0
    r = s
    for i in range(n-1):
        l += a[i]
        r -= a[i]
        ans = min(ans, abs(l-r))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(a[0:n])
    # print(a[1:n])
    # print(a[2:n])
    # print(a[3:n])
    ans = 10**9
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    max_num = max(sum(a[0:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:l+1]))
                    min_num = min(sum(a[0:i+1]), sum(a[i+1:j+1]), sum(a[j+1:k+1]), sum(a[k+1:l+1]))
                    if ans > max_num - min_num:
                        ans = max_num - min_num
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A_sum = sum(A)
    A_cumsum = [0]
    for i in range(N):
        A_cumsum.append(A_cumsum[i]+A[i])
    A_cumsum2 = [0]
    for i in range(N):
        A_cumsum2.append(A_cumsum2[i]+A[i]**2)

    ans = A_sum
    for i in range(1,N-2):
        for j in range(i+1,N-1):
            P = A_cumsum[i]
            Q = A_cumsum[j]-A_cumsum[i]
            R = A_cumsum[N]-A_cumsum[j]
            S = A_sum-P-Q-R
            ans = min(ans,max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 二分探索
    ans = float("inf")
    for i in range(2, N - 1):
        # P, Q, R, S の候補のうち、最大値と最小値の差が最小になるものを求める
        # P, Q, R, S の候補は、S[1:i], S[i:j], S[j:k], S[k:N] となる
        # 二分探索を行うために、S[i:j] の値が S[1:i] から最も近い値を二分探索で求める
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A[0])
    #print(A[1])

    #print(A)
    #print(A[1:])

    #print(A[:-1])
    #print(A[:])
    #print(A[-1:])
    #print(A[-1])
    #print(A[-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[2:-2])
    #print(A[2:-1])
    #print(A[1:-1])
    #print(A[1:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

    #print(A[1:-1])
    #print(A[1:-2])
    #print(A[2:-1])
    #print(A[2:-2])

=======
Suggestion 8

def process():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    l = 0
    r = s
    ans = float('inf')
    for i in range(n-1):
        l += a[i]
        r -= a[i]
        ans = min(ans, abs(l-r))
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)
    # N = 10
    # A = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]

    # N = 7
    # A = [1, 2, 3, 1000000000, 4, 5, 6]

    # N = 5
    # A = [3, 2, 4, 1, 2]

    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # N = 10
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000000000]

    # N = 10
    # A = [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # A = [1, 2, 3, 4, 5, 1000000000, 7, 8, 9, 10]

    # N = 10
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 1000000000, 1000000000]

    # N = 10
    # A = [1000000000, 1000000000, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # A = [1, 2, 1000000000,

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    l = 0
    r = s
    for i in range(n - 1):
        l += a[i]
        r -= a[i]
        ans = min(ans, abs(l - r))
    print(ans)
