Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (N-i-1)*(A[i+1]-A[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += (n - 1 - i) * (a[i+1] - a[i])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += N - (i + 1) - (A[i+1:] == A[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        if i == 0 or A[i] != A[i-1]:
            cnt += i
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        res += i - bisect.bisect_left(a, a[i])
    print(res)

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = n * (n - 1) // 2
    cnt = 1
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            cnt += 1
        else:
            ans -= cnt * (cnt - 1) // 2
            cnt = 1
    ans -= cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = Counter(A)
    ans = 0
    for i in C:
        ans += C[i] * (C[i] - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N):
        ans += (N - 1 - i) * i
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            ans -= N - 1 - i
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの要素をキーとした辞書を作成
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    # 重複する要素の組み合わせを計算
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2

    # 答えを出力
    print(N * (N - 1) // 2 - ans)

=======
Suggestion 10

def solve(N, A):
    # A_i ≠ A_j
    # A_i < A_j
    # A_i < A_k
    # A_j < A_k
    # A_i < A_j < A_k
    # A_i < A_j < A_k < A_l
    # A_i < A_j < A_k < A_l < A_m
    # A_i < A_j < A_k < A_l < A_m < A_n
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p < A_q

    # A_i < A_j < A_k
    # A_i < A_j < A_k < A_l
    # A_i < A_j < A_k < A_l < A_m
    # A_i < A_j < A_k < A_l < A_m < A_n
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p < A_q
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p < A_q < A_r

    # A_i < A_j < A_k
    # A_i < A_j < A_k < A_l
    # A_i < A_j < A_k < A_l < A_m
    # A_i < A_j < A_k < A_l < A_m < A_n
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p
    # A_i < A_j < A_k < A_l < A_m < A_n < A_o < A_p < A_q
    # A_i < A_j < A_k <
