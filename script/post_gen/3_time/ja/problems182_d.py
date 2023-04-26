Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans = max(ans, s)
        if s < 0:
            s = 0
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(N):
        if sum < 0:
            sum = 0
        sum += A[i]
        if max < sum:
            max = sum
    print(max)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
    print(max(A) - min(A))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    if A[0] > 0:
        ans += A[0]
    for i in range(N-1):
        if A[i+1] > 0:
            if A[i] < 0:
                ans += A[i+1]
            else:
                ans += A[i+1] - A[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    print(max(A))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MAX = 0
    for i in range(N):
        MAX += max(A[i], 0)
    for i in range(N):
        if A[i] >= 0:
            print(MAX)
        else:
            print(MAX - max(A[i], 0) + max(A[i + 1:], 0))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 進んだ距離の累積和を求める
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    # 累積和の最大値を求める
    A_sum_max = [0] * (N + 1)
    for i in range(N + 1):
        A_sum_max[i] = max(A_sum_max[i - 1], A_sum[i])
    # 累積和の最小値を求める
    A_sum_min = [0] * (N + 1)
    for i in range(N + 1):
        A_sum_min[i] = min(A_sum_min[i - 1], A_sum[i])
    # 最大値と最小値の差の最大値を求める
    ans = 0
    for i in range(N + 1):
        ans = max(ans, A_sum_max[i] - A_sum_min[i])
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))

    #Aの最大値を求める
    max_A = max(A)
    #print(max_A)
    #Aの最大値のindexを求める
    max_index = A.index(max_A)
    #print(max_index)
    #Aの最大値のindexまでの和を求める
    sum_A = sum(A[:max_index+1])
    #print(sum_A)
    #Aの最大値のindexから最後までの和を求める
    sum_A2 = sum(A[max_index+1:])
    #print(sum_A2)
    #Aの最大値のindexまでの和とAの最大値のindexから最後までの和の絶対値の大きい方を出力する
    print(max(sum_A, sum_A2))
