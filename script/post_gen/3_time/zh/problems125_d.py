Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    min_num = 10**9
    for i in range(n):
        if arr[i] < 0:
            cnt += 1
        arr[i] = abs(arr[i])
        min_num = min(min_num, arr[i])
    if cnt % 2 == 0:
        print(sum(arr))
    else:
        print(sum(arr) - 2 * min_num)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    cnt = 0
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            cnt += 1

    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - 2 * min(abs(x) for x in a))

=======
Suggestion 3

def solver1():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i - 1] - b[i - 1]
    print(*b)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        if A[i] < 0:
            sum += -A[i]
        else:
            sum += A[i]
    if A[0] < 0:
        if N % 2 == 0:
            sum -= 2 * A[0]
        else:
            sum += 2 * A[0]
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    sum = 0
    minus = 0
    min_abs = float('inf')
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus += 1
        min_abs = min(min_abs, abs(a[i]))
    if minus % 2 == 0:
        ans = sum
    else:
        ans = sum - 2 * min_abs
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
            a[i] = -a[i]
        ans += a[i]
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(a) * 2)

solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(sum(A))
    else:
        print(sum(A[1:]) - A[0])

=======
Suggestion 8

def get_max_sum(n, a):
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不用管
    #如果有正数，那么正数全都取正号；如果没有正数，那么全都取负号
    #如果有0，那么可以不用管；如果全是负数，那么可以不

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(abs(a[i]) for i in range(n)) * 2)

=======
Suggestion 10

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
        print(ans - abs(min(a)) * 2)
