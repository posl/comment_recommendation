Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N-1):
        if A[i] < 0:
            count += 1
            A[i] *= -1
        if A[i+1] < 0:
            count += 1
            A[i+1] *= -1
    if count % 2 == 0:
        print(sum(A))
    else:
        print(sum(A) - 2*min(A))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum([abs(i) for i in a]))
    else:
        print(sum([abs(i) for i in a]) - 2 * abs(a[0]))

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] >= 0:
        return sum(a) - 2 * a[0]
    elif a[-1] <= 0:
        return 2 * abs(a[-1]) - sum(a)
    else:
        return sum(map(abs, a))

print(solve())

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(x) for x in a]
    if sum([1 for x in a if x < 0]) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] < 0:
        if n % 2 == 0:
            print(sum(map(abs, a)))
        else:
            print(sum(map(abs, a)) - 2*abs(a[0]))
    else:
        print(sum(a))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] < 0 and a[-1] < 0:
        a = [-i for i in a]
    if a[0] < 0 and a[-1] > 0:
        a = [-i for i in a]
        print(sum(a) + 2 * a[0])
    if a[0] > 0 and a[-1] > 0:
        print(sum(a) - 2 * a[0])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    ans = sum(a)
    if a[0] < 0:
        ans -= 2*a[0]
    elif a[0] == 0:
        ans = 0
    else:
        ans -= 2*a[0]
        if a.count(0) % 2 == 1:
            ans = ans + 2*a[0]

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum_a = sum(abs(x) for x in a)
    if a[0] < 0:
        sum_a -= 2 * a[0]
    elif a[0] == 0:
        pass
    else:
        sum_a += 2 * a[0]
    print(sum_a)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # a = [int(i) for i in input().split()]
    # a = input().split()
    # a = list(map(int, input().split()))

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    # a = [int(input()) for i in range(n)]
    # a = [input() for i in range(n)]
    # a = [list(map(int, input())) for i in range(n)]

    ans = 0
    c = 0
    m = 1000000000
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            c += 1
