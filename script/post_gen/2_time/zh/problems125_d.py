Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    ans = 0
    minus = 0
    min_abs = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
        ans += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if minus % 2 == 0:
        return ans
    else:
        return ans - 2 * min_abs

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for a in A:
        if a < 0:
            cnt += 1
            a = -a
        ans += a
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(A) * 2)

=======
Suggestion 3

def max_sum(a):
    sum = 0
    minus_count = 0
    min_abs = 10**9+1
    for i in range(len(a)):
        if a[i] < 0:
            minus_count += 1
        sum += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if minus_count % 2 == 0:
        return sum
    else:
        return sum - min_abs*2

=======
Suggestion 4

def get_max_sum(n, a):
    max_sum = 0
    count = 0
    for i in range(n):
        if a[i] < 0:
            count += 1
            a[i] = -a[i]
        max_sum += a[i]
    if count % 2 == 0:
        return max_sum
    else:
        return max_sum - 2 * min(a)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
            a[i] = -a[i]
    if cnt % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - 2 * min(a))

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N == 2:
        if A[0] < 0 and A[1] < 0:
            print(-A[0]-A[1])
        elif A[0] < 0 and A[1] > 0:
            print(A[1]-A[0])
        else:
            print(A[0]+A[1])
        return
    elif N == 1:
        print(A[0])
        return
    else:
        count = 0
        for i in range(N):
            if A[i] < 0:
                count += 1
        if count % 2 == 0:
            print(sum([abs(i) for i in A]))
        else:
            print(sum([abs(i) for i in A]) - 2*min([abs(i) for i in A]))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(sum(A))
    else:
        print(sum(A) - 2 * A[0])

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(map(abs, a))
    cnt = 0
    for i in a:
        if i < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(s)
    else:
        print(s - 2 * min(map(abs, a)))

solve()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
    a = list(map(abs, a))
    if cnt % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - min(a) * 2)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        if a < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(sum(map(abs, A)))
    else:
        print(sum(map(abs, A)) - min(map(abs, A)) * 2)
