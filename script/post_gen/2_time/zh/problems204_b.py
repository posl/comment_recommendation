Synthesizing 10/10 solutions

=======
Suggestion 1

def get_nuts(nuts):
    nuts.sort()
    nuts.reverse()
    nuts.pop(0)
    return sum(nuts)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

=======
Suggestion 3

def get_nuts(nuts):
    nuts = [int(nut) for nut in nuts.split(' ')]
    nuts.sort()
    nuts.reverse()
    nuts = [nut - 10 for nut in nuts]
    nuts = [nut if nut > 0 else 0 for nut in nuts]
    return sum(nuts)

=======
Suggestion 4

def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    #处理
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    #输出
    print(ans)

=======
Suggestion 5

def get_nut():
    n = int(input())
    nut = list(map(int, input().split()))
    return n, nut

=======
Suggestion 6

def get_nuts_number(nuts):
    nuts_number = 0
    for nut in nuts:
        if nut > 10:
            nuts_number += nut - 10
    return nuts_number

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] > 10:
            count += A[i] - 10
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if a[i] > 10:
            sum += a[i] - 10
    print(sum)

=======
Suggestion 10

def main():
    num = int(input())
    nuts = list(map(int, input().split()))
    total = 0
    for nut in nuts:
        if nut >= 10:
            total += nut - 10
    print(total)
