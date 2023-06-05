Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if a[i] > 10:
            result += a[i] - 10
    print(result)

=======
Suggestion 3

def get_nut(nut):
    if nut >= 10:
        return nut - 10
    else:
        return 0

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)

=======
Suggestion 5

def get_nuts(nuts):
    sum = 0
    for nut in nuts:
        if nut > 10:
            sum += nut - 10
    return sum

=======
Suggestion 6

def get_nuts(nuts):
    total = 0
    for nut in nuts:
        if nut > 10:
            total += nut - 10
    return total

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] > 10:
            total += A[i] - 10
    print(total)

=======
Suggestion 8

def problems204_b():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

problems204_b()

=======
Suggestion 9

def problem204_b():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([max(A[i]-10, 0) for i in range(N)]))

=======
Suggestion 10

def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    nuts.sort()
    nuts.reverse()
    result = 0
    for i in range(num):
        if i % 2 == 0:
            result += nuts[i]
    print(result)
