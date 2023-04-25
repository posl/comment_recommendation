Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i] * A[j]
    print(sum % (10**9 + 7))

=======
Suggestion 2

def main():
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    ans = 0
    for a in A:
        sumA -= a
        ans += a * sumA
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * A[i]
        ans %= 10**9+7
    ans *= N * (N-1) // 2
    ans %= 10**9+7
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N-1):
        ans += A[i]*(A[i+1]*i - A[i]*(N-1-i))
        ans %= 10**9+7
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = [int(a) for a in input().split()]
    s = sum(A)
    ans = 0
    for a in A:
        s -= a
        ans += a * s
        ans %= 1000000007

    print(ans)

solve()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i] * a[i]
    print(s % (10 ** 9 + 7))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = (C[i] + A[i]) % (10 ** 9 + 7)

    ans = 0
    for i in range(N):
        ans += A[i] * (C[N] - C[i + 1])
        ans %= (10 ** 9 + 7)

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7

    # 累積和
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = (s[i - 1] + A[i - 1]) % MOD

    ans = 0
    for i in range(N):
        ans += A[i] * (s[N] - s[i + 1])
        ans %= MOD

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    # 1. A_i x A_jを求める
    # 2. それを合計する
    # 3. それを合計する
    # 4. それをMODで割る
    # 1. と 2. をまとめると、A_i x A_jを合計する
    # 3. と 4. をまとめると、A_i x A_jを合計したものをMODで割る
    # 1. と 3. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 2. と 3. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 2. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 2. と 3. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 2. と 3. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 2. と 3. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 2. と 3. と 4. をまとめると、A_i x A_jの合計を求め、それをMODで割る
    # 1. と 2. と 3. と

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    # 1. 配列Aの和を求める
    sum_A = sum(A)

    # 2. 配列Aの要素の和を求める
    sum_A2 = sum([a * a for a in A])

    # 3. 配列Aの要素の和を求める
    sum_A3 = sum([a * a * a for a in A])

    # 4. 配列Aの要素の和を求める
    sum_A4 = sum([a * a * a * a for a in A])

    # 5. 配列Aの要素の和を求める
    sum_A5 = sum([a * a * a * a * a for a in A])

    # 6. 配列Aの要素の和を求める
    sum_A6 = sum([a * a * a * a * a * a for a in A])

    # 7. 配列Aの要素の和を求める
    sum_A7 = sum([a * a * a * a * a * a * a for a in A])

    # 8. 配列Aの要素の和を求める
    sum_A8 = sum([a * a * a * a * a * a * a * a for a in A])

    # 9. 配列Aの要素の和を求める
    sum_A9 = sum([a * a * a * a * a * a * a * a * a for a in A])

    # 10. 配列Aの要素の和を求める
    sum_A10 = sum([a * a * a * a * a * a * a * a * a * a for a in A])

    # 11. 配列Aの要素の和を求める
    sum_A11 = sum([a * a * a * a * a * a * a * a * a * a * a for a in A])

    # 12. 配列Aの要素の和を求
