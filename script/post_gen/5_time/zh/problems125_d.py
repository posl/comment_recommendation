Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in a:
        if i < 0:
            cnt += 1

    if cnt % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - min(map(abs, a)) * 2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
            a[i] *= -1
        ans += a[i]
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(a) * 2)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if A[i] < 0:
            B.append(-A[i])
        else:
            B.append(A[i])
    if sum(A) >= 0:
        print(sum(B))
    else:
        print(sum(B) - 2 * min(B))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - 2*min(abs(i) for i in a))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    minus = 0
    for i in range(n):
        if a[i] < 0:
            minus += 1
    if minus % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - min(map(abs, a)) * 2)

=======
Suggestion 6

def max_sum(n, a):
    if n == 1:
        return a[0]
    if n == 2:
        return max(a[0] + a[1], a[0] - a[1], -a[0] + a[1], -a[0] - a[1])
    if n == 3:
        return max(a[0] + a[1] + a[2], a[0] + a[1] - a[2], a[0] - a[1] + a[2], a[0] - a[1] - a[2], \
                   -a[0] + a[1] + a[2], -a[0] + a[1] - a[2], -a[0] - a[1] + a[2], -a[0] - a[1] - a[2])
    if n == 4:
        return max(a[0] + a[1] + a[2] + a[3], a[0] + a[1] + a[2] - a[3], a[0] + a[1] - a[2] + a[3], a[0] + a[1] - a[2] - a[3], \
                   a[0] - a[1] + a[2] + a[3], a[0] - a[1] + a[2] - a[3], a[0] - a[1] - a[2] + a[3], a[0] - a[1] - a[2] - a[3], \
                   -a[0] + a[1] + a[2] + a[3], -a[0] + a[1] + a[2] - a[3], -a[0] + a[1] - a[2] + a[3], -a[0] + a[1] - a[2] - a[3], \
                   -a[0] - a[1] + a[2] + a[3], -a[0] - a[1] + a[2] - a[3], -a[0] - a[1] - a[2] + a

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sign = 1
    a_sum = 0
    min_abs = 10**10
    for i in range(n):
        a_sum += abs(a[i])
        if a[i] < 0:
            sign *= -1
        min_abs = min(min_abs, abs(a[i]))
    if sign == 1:
        print(a_sum)
    else:
        print(a_sum - 2 * min_abs)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    minus = 0
    min_num = 10**9 + 1
    sum = 0
    for i in range(N):
        sum += abs(A[i])
        if A[i] < 0:
            minus += 1
        if abs(A[i]) < min_num:
            min_num = abs(A[i])
    if minus % 2 == 0:
        print(sum)
    else:
        print(sum - 2*min_num)

=======
Suggestion 9

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [abs(x) for x in a]
    c = [x for x in a if x < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_abs = list(map(abs, a))
    a_sum = sum(a_abs)
    a_abs_min = min(a_abs)
    if a_abs_min in a:
        if a_sum % 2 == 0:
            print(a_sum)
        else:
            print(a_sum - a_abs_min * 2)
    else:
        print(a_sum)
