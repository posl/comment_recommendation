Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    B = A*(10**100)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            exit()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    k = x // s
    r = x % s
    i = 0
    while r >= 0:
        r -= a[i]
        i += 1
    print(k * n + i)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    B = A * 10**100
    S = [0] * len(B)
    S[0] = B[0]
    for i in range(1, len(B)):
        S[i] = S[i-1] + B[i]
        if S[i] > X:
            print(i+1)
            break

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    sumA = sum(A)
    n = X // sumA
    x = X % sumA

    sumB = 0
    for i in range(N):
        sumB += A[i]
        if sumB > x:
            print(n * N + i + 1)
            break

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    count = x // sum_a
    x = x % sum_a
    sum_a = 0
    for i in range(n):
        sum_a += a[i]
        count += 1
        if sum_a > x:
            break
    print(count)

=======
Suggestion 6

def problem():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10 ** 100
    sum = 0
    count = 0
    for i in range(len(B)):
        sum += B[i]
        count += 1
        if sum > X:
            print(count)
            break

=======
Suggestion 7

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a_list)
    a_len = len(a_list)
    b_len = (x // a_sum) * a_len
    b_sum = (x // a_sum) * a_sum
    for a in a_list:
        b_len += 1
        b_sum += a
        if b_sum > x:
            break
    print(b_len)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a*100
    s = sum(b)
    k = x//s*len(b)
    r = x%s
    for i in range(len(b)):
        if r < 0:
            break
        r -= b[i]
        k += 1
    print(k)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    # 10^100 個の A が連結されている
    # つまり、10^100 個の A の総和が X を超える最小の k を求める
    # 10^100 個の A の総和は、10^100 個の A の総和の 1 周分の総和を求めて、
    # 10^100 個の A の総和の 1 周分の総和を 10^100 で割ることで求めることができる
    # 10^100 個の A の総和の 1 周分の総和は、A の総和を 10^100 個足したものに等しい
    # よって、10^100 個の A の総和は、A の総和を 10^100 で割ったものに等しい
    # 10^100 個の A の総和は、X を超える最小の k は、
    # X を A の総和を 10^100 で割ったものの切り上げに等しい
    # つまり、math.ceil(x / sum(a)) が答え

    import math
    print(n * math.ceil(x / sum(a)))

=======
Suggestion 10

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])
