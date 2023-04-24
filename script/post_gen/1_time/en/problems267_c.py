Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    for i in range(M):
        ans += (i+1) * A[i]
    tmp = ans
    for i in range(N-M):
        tmp = tmp + (M+1) * A[i+M] - S[i+M+1] + S[i+1]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])
    print(max(B))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] * (N - 1)
    for i in range(N - 1):
        B[i] = A[i + 1] - A[i]

    #print(B)

    ans = 0
    for i in range(N - M):
        ans += max(0, sum(B[i : i + M]))

    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [-3, 1, -4, 1, -5, 9, -2, 6, -5, 3]
    #N = 10
    #M = 4
    #A = [5, 4, -1, 8]
    #N = 4
    #M = 2
    #A = [1, 2, 3, 4]
    #N = 4
    #M = 3
    #A = [4, 3, 2, 1]
    #N = 4
    #M = 3
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 3
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 4
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 5
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 6
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 7
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 8
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 9
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 10
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 11
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 12
    #A = [1, 2, 3, -4]
    #N = 4
    #M = 13
    #A = [1,

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum(a[i:i+m]))
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - m + 1):
        b.append(sum(a[i:i + m]))
    print(sum(sorted(b, reverse=True)[:m]))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(A[i])
        if i >= M:
            B[i] += B[i - M]
    B.sort(reverse=True)
    print(sum(B[:M]))

main()

The following code is the solution to the following problem.

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    B = []
    for i in range(M):
        B.append(A[i])
    B.sort(reverse=True)
    #print(B)
    ans = 0
    for i in range(M):
        ans += (i+1) * B[i]
    print(ans)

=======
Suggestion 9

def main():
    import sys
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A = list(map(int, sys.stdin.read().split()))
    # N, M = A[0], A[1]
    # A = A[2:]
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        for j in range(M):
            B[i] += (j + 1) * A[i + j]
    print(max(B))

=======
Suggestion 10

def main():
    #input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    
    #compute
    #前処理
    #As[i]をi+1番目の要素として、累積和を求める
    As = [0] + As
    for i in range(N):
        As[i+1] += As[i]
    
    #最大値の計算
    max_sum = 0
    for i in range(N-M+1):
        max_sum = max(max_sum, As[i+M]-As[i])
    
    #output
    print(max_sum)
