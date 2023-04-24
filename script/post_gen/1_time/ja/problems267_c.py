Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[-1] + A[i])

    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sumA[i+M] - sumA[i] + M*(M-1))

    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1]+a)
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, S[i+M]-S[i])
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans, sum([(j+1)*A[i+j] for j in range(M)]))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N-M+1):
        ans = max(ans, sum([j*A[i+j] for j in range(M)]))
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])

    # 累積和の差分を求める
    diff = []
    for i in range(N - M + 1):
        diff.append(sumA[i + M] - sumA[i])

    # 累積和の差分の最大値を求める
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, diff[i] + i * M)

    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum((i+1)*A[i] for i in range(M)))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # 累積和
    for i in range(1, N+1):
        A[i] += A[i-1]
    ans = 0
    # 累積和の差分を取り、M個ずつの和の最大値を取る
    for i in range(N-M+1):
        ans = max(ans, A[i+M]-A[i])
    print(ans)

=======
Suggestion 8

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-M+1):
        sum += sum(A[i:i+M])
    print(sum)
    return

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #B = A[0:M]
    B = A[0:M]
    #print(B)
    #print(sum(B))
    #print(sum(i * B[i] for i in range(len(B))))
    ans = sum(i * B[i] for i in range(len(B)))
    for i in range(1, N - M + 1):
        B = A[i:i + M]
        #print(B)
        #print(sum(B))
        #print(sum(i * B[i] for i in range(len(B))))
        ans = max(ans, sum(i * B[i] for i in range(len(B))))
    print(ans)

=======
Suggestion 10

def main():
    # 入力
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    # 処理
    # 連続部分列の長さmの場合のsum_{i=1}^{M} i × B_iの最大値を求める
    # 連続部分列B=(B_1,B_2,...,B_M)の場合のsum_{i=1}^{M} i × B_iの最大値は、
    # sum_{i=1}^{M} i × B_i = B_1 + B_2 + ... + B_M + (1 + 2 + ... + M) - M
    # なので、B_1 + B_2 + ... + B_Mの最大値を求めれば良い

    # B_1 + B_2 + ... + B_Mの最大値を求める
    # A_1 + A_2 + ... + A_M
    # A_2 + A_3 + ... + A_(M+1)
    # A_3 + A_4 + ... + A_(M+2)
    # ...
    # A_(N-M+1) + A_(N-M+2) + ... + A_N
    # の中で最大値を求めれば良い
    # これは、A_1 + A_2 + ... + A_M
    # A_1 + A_2 + ... + A_M + A_(M+1)
    # A_1 + A_2 + ... + A_M + A_(M+1) + A_(M+2)
    # ...
    # A_1 + A_2 + ... + A_M + A_(M+1) + ... + A_(N-M)
    # A_1 + A_2 + ... + A_M + A_(M+1) + ... + A_(N-M) + A_(N-M+1)
    # ...
    # A_1 + A_2 + ... + A_M + A_(M+1) + ... + A_(N-M) + A_(N-M+1) + ... + A_N
