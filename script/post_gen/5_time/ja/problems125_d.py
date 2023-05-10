Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1, n):
        if a[i-1] * a[i] < 0:
            if a[i-1] < 0:
                sum += -a[i-1]
                a[i-1] = 0
            else:
                sum += a[i]
                a[i] = 0
    if a[n-1] < 0:
        sum += -a[n-1]
        a[n-1] = 0
    else:
        sum += a[n-1]
        a[n-1] = 0
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] < 0:
            ans += abs(a[i])
            a[i] = 0
        if a[i+1] < 0:
            ans += abs(a[i+1])
            a[i+1] = 0
    print(ans + sum(a))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    minus = 0
    min_minus = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
            if min_minus > -a[i]:
                min_minus = -a[i]
        ans += abs(a[i])
    if minus % 2 == 1:
        ans -= 2 * min_minus
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i]+A[i+1] < 0:
            ans += 2*min(A[i], A[i+1])
            A[i] = 0
            A[i+1] = 0
    print(ans + sum(A))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    minus = 0
    for i in range(n-1):
        if a[i] < 0:
            minus += 1
        if minus % 2 == 0:
            ans += abs(a[i])
        else:
            ans -= abs(a[i])
        a[i+1] += a[i]
    if minus % 2 == 0:
        ans += a[-1]
    else:
        ans -= a[-1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        ans += abs(a[i] - a[i+1])

    ans += abs(a[0])
    ans += abs(a[n-1])

    for i in range(n-1):
        if i == 0:
            print(ans - abs(a[i]) - abs(a[i] - a[i+1]) + abs(a[i+1]))
        elif i == n-2:
            print(ans - abs(a[i] - a[i+1]) - abs(a[i+1]) + abs(a[i]))
        else:
            print(ans - abs(a[i] - a[i+1]) - abs(a[i+1]) - abs(a[i] - a[i-1]) + abs(a[i+1] - a[i-1]))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] < 0:
            A[i] *= -1
            A[i+1] *= -1
    print(sum(A))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    minus = 0
    min_minus = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
            a[i] *= -1
        if a[i] < min_minus:
            min_minus = a[i]
        ans += a[i]
    if minus%2 == 0:
        print(ans)
    else:
        print(ans - min_minus*2)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 偶数番目の総和を計算
    even_sum = sum([a[i] for i in range(n) if i % 2 == 0])
    # 偶数番目の総和と奇数番目の総和の差分
    diff = [even_sum - sum(a[1::2])]
    # 差分の絶対値の最大値
    max_abs_diff = diff[0]
    for i in range(n - 1):
        # i 番目の要素を -1 倍する
        diff.append(diff[-1] + 2 * a[i])
        # 差分の絶対値の最大値を更新する
        max_abs_diff = max(max_abs_diff, abs(diff[-1]))
    # 偶数番目の総和と奇数番目の総和の差分に最大値を加算したものが答え
    print(even_sum + max_abs_diff)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] < 0:
            A[i] *= -1
        if A[i+1] < 0:
            A[i+1] *= -1
        ans += A[i+1] - A[i]
    print(ans)
