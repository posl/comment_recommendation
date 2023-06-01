Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1

    if cnt % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - 2 * min(map(abs, a)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += abs(a[i])
    if a[0] < 0:
        a[0] = -a[0]
    for i in range(1, n):
        if a[i] < 0:
            a[i] = -a[i]
        if a[i-1] < a[i]:
            a[i-1], a[i] = a[i], a[i-1]
    if n % 2 == 0:
        print(sum)
    else:
        print(sum - 2*a[n-1])
main()

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minus_cnt = 0
    min_abs = 10**9
    sum = 0
    for i in range(n):
        if a[i] < 0:
            minus_cnt += 1
        abs_a = abs(a[i])
        if min_abs > abs_a:
            min_abs = abs_a
        sum += abs_a
    if minus_cnt % 2 == 0:
        print(sum)
    else:
        print(sum - min_abs * 2)

solve()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(sum(A) - 2 * A[0])
    elif A[-1] <= 0:
        print(-sum(A) + 2 * A[-1])
    else:
        print(sum(map(abs, A)))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0:
        if N % 2 == 0:
            print(sum(A))
        else:
            print(sum(A) - 2 * A[0])
    else:
        print(sum(A) - 2 * A[0])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    min = 1000000000
    count = 0
    for i in range(N):
        sum += abs(A[i])
        if A[i] < 0:
            count += 1
        if abs(A[i]) < min:
            min = abs(A[i])
    if count % 2 == 0:
        print(sum)
    else:
        print(sum - min * 2)

=======
Suggestion 7

def problem125_d():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    minus_count = 0
    min_abs = 10**9 + 1
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus_count += 1
        if min_abs > abs(a[i]):
            min_abs = abs(a[i])
    if minus_count % 2 == 0:
        print(sum)
    else:
        print(sum - 2 * min_abs)

problem125_d()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N

    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]

    for i in range(1, N):
        B[i] = 2 * A[i - 1] - B[i - 1]

    print(*B)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    # 负数的个数
    neg = 0
    # 绝对值最小的数
    min_abs = 10**9 + 1
    # 绝对值之和
    sum_abs = 0
    # 计算负数的个数，并且求出绝对值最小的数
    for i in range(N):
        if A[i] < 0:
            neg += 1
        if abs(A[i]) < min_abs:
            min_abs = abs(A[i])
        sum_abs += abs(A[i])
    # 如果负数的个数是偶数，则直接输出绝对值之和
    if neg % 2 == 0:
        print(sum_abs)
    # 如果负数的个数是奇数，则将绝对值之和减去两个最小的绝对值之和
    else:
        print(sum_abs - 2 * min_abs)
