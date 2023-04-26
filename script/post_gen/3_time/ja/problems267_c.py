Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 0
    for i in range(M, N + 1):
        ans = max(ans, S[i] - S[i - M])
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum(A[i:i+M]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (i+1) * A[i] - (N-i) * A[i]
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum([a[i+j]*(j+1) for j in range(m)]))
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max([sum(A[i:i+M]) * (i+1) for i in range(N-M+1)]))

=======
Suggestion 6

def main():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum(A[i:i+M]) + sum(range(1, M+1)))
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for i in range(M):
        B[i] = sum(A[i:N-M+i+1])
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i+1) * B[i]
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = (i+1)*A[i] - (N-i)*A[i]
    B.sort(reverse=True)
    print(sum(B[:M]))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和をとる
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    # 1つ目の累積和のみを使って、M個の要素の和を求める
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, S[i+M] - S[i])

    # 2つ目の累積和を使って、M個の要素の和を求める
    # 2つ目の累積和は、M個の要素の和を求める際に、
    # 1つ目の累積和のM個の要素の和から、1つ目の累積和の1個の要素を引いた値になる
    # 1つ目の累積和のM個の要素の和は、1つ目の累積和のM個の要素の和から、1つ目の累積和の1個の要素を引いた値になる
    # 1つ目の累積和の1個の要素は、1つ目の累積和の1個の要素から、1つ目の累積和の1個の要素を引いた値になる
    # つまり、1つ目の累積和の1個の要素は、0になる
    # 1つ目の累積和のM個の要素の和は、0になる
    # つまり、2つ目の累積和のM個の要素の和は、1つ目の累積和のM個の要素の和になる
    # 1つ目の累積和のM個の要

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print(A[1:3])
    sum_A = [0]
    for i in range(N):
        sum_A.append(sum_A[i] + A[i])
    #print(sum_A)
    max_sum = 0
    for i in range(M, N+1):
        #print(i)
        #print(sum_A[i-M:i])
        sum_B = sum_A[i] - sum_A[i-M]
        #print(sum_B)
        if max_sum < sum_B:
            max_sum = sum_B
    #print(max_sum)
    ans = 0
    for i in range(M):
        ans += (i+1) * max_sum
    print(ans)
