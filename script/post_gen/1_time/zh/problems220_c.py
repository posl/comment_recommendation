Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    total = sum(a)
    k = (x // total) * n
    x %= total
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        k += 1
    print(k)

solve()

=======
Suggestion 2

def get_input():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())
    return N, A, X

=======
Suggestion 3

def problem220_c():
    pass

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    sum_a = sum(a)
    sum_b = sum_a * (10 ** (100 - 1))
    if sum_b <= x:
        print(10 ** 100)
        return

    sum_b -= sum_a
    d = (x - sum_b) // sum_a
    print(100 * d + 1)


solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = []
    for i in range(100):
        B.extend(A)
    sum = 0
    k = 0
    for i in range(len(B)):
        sum += B[i]
        k = i
        if sum > X:
            break
    print(k+1)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())
    B = A * 100
    sum = 0
    for i in range(100 * N):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    b = a * 100
    s = 0
    for i in range(len(b)):
        s += b[i]
        if s > x:
            print(i+1)
            break

=======
Suggestion 8

def sum(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum

=======
Suggestion 9

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    x = int(input())
    x_10_100 = x * 10**100
    sum_a = sum(a)
    sum_b = sum_a * 10**100
    if sum_b <= x_10_100:
        print(10**100)
        return
    sum_b = 0
    k = 0
    while True:
        sum_b += a[k % n]
        if sum_b > x_10_100:
            break
        k += 1
    print(k + 1)
