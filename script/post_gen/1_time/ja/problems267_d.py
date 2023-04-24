Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N-M+1):
        B.append(sum(A[i:i+M]))
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i+1)*B[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N-M+1):
        B.append(sum(A[i:i+M]))
    print(max(B))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(N - M + 1):
        B.append(sum(A[i:i + M]))
    B.sort(reverse = True)
    print(sum([B[i] * (i + 1) for i in range(M)]))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    ans = -float('inf')
    for i in range(n-m+1):
        for j in range(i+m, n+1):
            ans = max(ans, sum_a[j]-sum_a[i] + (j-i)*sum(a[i:j]))
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            B = A[i:j+1]
            if len(B) == M:
                tmp = 0
                for k in range(M):
                    tmp += (k+1)*B[k]
                ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, sum(A[i:i+j+1]) + sum(range(1, j+2)))
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        b = a[i:i+m]
        if len(b) == m:
            ans = max(ans, sum([j * b[j-1] for j in range(1, m+1)]))
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)

    #sum_{i=1}^{M} i × B_i の最大値を求める
    #B=(B_1,B_2,...,B_M)
    #sum_{i=1}^{M} i × B_i = sum_{i=1}^{M} i × A_{i+j-1}
    #i+j-1がM以下であるi,jの組み合わせを全て試す
    #i+j-1がM以下であるi,jの組み合わせの個数は、
    #i+j-1がM以下のiの個数×jの個数
    #iが1からMまでの時、i+j-1がM以下のjの個数は、
    #M-(i+j-1)+1=M-i+1
    #よって、sum_{i=1}^{M} i × B_i = sum_{i=1}^{M} i × A_{i+j-1} = sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1}
    #sum_{i=1}^{M} i × B_i の最大値は、
    #sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1} の最大値
    #sum_{i=1}^{M} i × sum_{j=1}^{M-i+1} A_{i+j-1} = sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1}
    #sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1} の最大値を求める
    #sum_{j=1}^{M} sum_{i=1}^{M-j+1} i × A_{i+j-1}

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. Aの累積和を求める
    # 2. 1.の累積和の差を求める
    # 3. 2.の差の累積和の最大値を求める
    # 4. 3.の最大値を出力
    # 1.
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    # 2.
    A_diff = [0] * N
    for i in range(N - 1):
        A_diff[i + 1] = A_sum[i + 1] - A_sum[i]
    # 3.
    A_diff_sum = [0] * (N + 1)
    for i in range(N):
        A_diff_sum[i + 1] = A_diff_sum[i] + A_diff[i]
    # 4.
    max_sum = 0
    for i in range(M, N + 1):
        max_sum = max(max_sum, A_diff_sum[i] - A_diff_sum[i - M])
    print(max_sum)
