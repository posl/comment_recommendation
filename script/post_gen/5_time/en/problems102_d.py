Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 1 << 60
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            p = s[i + 1]
            q = s[j + 1] - s[i + 1]
            r = s[n] - s[j + 1]
            m = max(p, q, r)
            mi = min(p, q, r)
            ans = min(ans, m - mi)
    print(ans)

solve()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cum = [0] * (n+1)
    for i in range(n):
        cum[i+1] = cum[i] + a[i]
    ans = 10**9
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            p = cum[i+1]
            q = cum[j+1] - cum[i+1]
            r = cum[n] - cum[j+1]
            s = cum[n] - cum[j+1]
            ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    S = [0] * (N + 2)
    for i in range(N + 1):
        S[i + 1] = S[i] + abs(A[i] - A[i + 1])
    def cost(i, j):
        return S[j] - S[i]
    def solve():
        left = 0
        right = 3
        while right < N:
            if cost(left, left + 2) < cost(right - 2, right):
                left += 1
            else:
                right += 1
        ans = 10 ** 18
        for i in range(left, right):
            for j in range(i + 1, right + 1):
                ans = min(ans, max(cost(left, i), cost(i, j), cost(j, right)))
        return ans
    print(solve())
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]
    for i in a:
        b.append(b[-1] + i)
    ans = float('inf')
    for i in range(1, n - 2):
        j = bisect.bisect_left(b, b[i] / 2)
        k = bisect.bisect_left(b, (b[i] + b[-1]) / 2)
        ans = min(ans, abs(b[i] - 2 * b[j]), abs(b[i] - 2 * (b[k] - b[i])))
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    r = float('inf')
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            p = s[i]
            q = s[j] - s[i]
            r = s[n] - s[j]
            s1 = max(p, q, r)
            s2 = min(p, q, r)
            r = min(r, s1 - s2)
    print(r)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(0, N):
        S.append(S[-1] + A[i])
    res = 10**9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            res = min(res, abs(S[i] - S[0] - (S[j] - S[i])) + abs(S[-1] - S[j] - (S[i + 1] - S[j])))
    print(res)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    min_diff = 10 ** 9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                B = A[0:i]
                C = A[i:j]
                D = A[j:k]
                E = A[k:N]
                P = sum(B)
                Q = sum(C)
                R = sum(D)
                S = sum(E)
                max_val = max(P, Q, R, S)
                min_val = min(P, Q, R, S)
                diff = max_val - min_val
                if diff < min_diff:
                    min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    total = sum(A)
    ans = 100000000000000000
    a = 0
    for i in range(N-1):
        a += A[i]
        ans = min(ans, abs(total-a-a))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #最初に全ての合計を出しておく
    sum_all = sum(A)

    #連続する部分列の合計を出しておく
    sum_part = []
    sum_part.append(A[0])
    for i in range(1,N):
        sum_part.append(sum_part[i-1] + A[i])

    #最初の一回目のカットで3つの部分列に分ける
    #最初のカットの場所は1番目からN-2番目までのN-2通り
    min_diff = 10**9
    for i in range(1,N-2):
        #1回目のカットで分けた部分列の合計を出す
        sum_1 = sum_part[i-1]
        sum_2 = sum_part[N-1] - sum_part[i-1]

        #2回目のカットで分けた部分列の合計を出す
        #2回目のカットの場所はi番目からN-1番目までのN-1-i通り
        for j in range(i+1,N-1):
            sum_3 = sum_part[j-1] - sum_part[i-1]
            sum_4 = sum_part[N-1] - sum_part[j-1]

            #最後のカットで分けた部分列の合計を出す
            sum_5 = sum_all - sum_1 - sum_2 - sum_3 - sum_4

            #最大値と最小値を求める
            max_value = max(sum_1,sum_2,sum_3,sum_4,sum_5)
            min_value = min(sum_1,sum_2,sum_3,sum_4,sum_5)

            #最大値と最小値の差を求める
            diff = max_value - min_value

            #最大値と最小値の差の最小値を求める
            min_diff = min(min_diff,diff)

    #結果を出力する
    print(min_diff)

=======
Suggestion 10

def run():
    N = int(input())
    A = [int(x) for x in input().split()]

    #print(N, A)

    S = sum(A)
    #print(S)

    #print(A)
    #print(A[:2])
    #print(A[2:])
    #print(A[:-2])
    #print(A[-2:])

    cut1 = [A[0:1], A[1:]]
    cut2 = [A[:-1], A[-1:]]

    #print(cut1)
    #print(cut2)

    #print(cut1[0], cut1[1], cut2[0], cut2[1])

    sum1 = sum(cut1[0]) + sum(cut1[1])
    sum2 = sum(cut2[0]) + sum(cut2[1])
    #print(sum1, sum2)

    print(max(sum1, sum2) - min(sum1, sum2))
