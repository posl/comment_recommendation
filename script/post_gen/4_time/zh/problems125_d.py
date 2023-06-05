Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(sum(a))
    else:
        print(sum(a[1:]) - a[0] * 2)

=======
Suggestion 2

def solve(n, a):
    sum = 0
    minus = 0
    absmin = 1000000000
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus += 1
        if abs(a[i]) < absmin:
            absmin = abs(a[i])
    if minus % 2 == 0:
        return sum
    else:
        return sum - 2*absmin

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if N == 2:
        print(A[1] - A[0])
        return
    if A[0] >= 0:
        print(sum(A) - 2 * A[0])
        return
    if A[-1] <= 0:
        print(-sum(A) + 2 * A[-1])
        return
    print(sum([abs(i) for i in A]))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += abs(A[i])
    if A[0] < 0:
        sum -= 2 * A[0]
    elif A[-1] > 0:
        sum -= 2 * A[-1]
    print(sum)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    minus = 0
    abs_a = []
    for i in range(n):
        if a[i] < 0:
            minus += 1
        abs_a.append(abs(a[i]))
    if minus % 2 == 0:
        print(sum(abs_a))
    else:
        print(sum(abs_a) - 2 * min(abs_a))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    minus = 0
    for i in range(N):
        ans += abs(A[i])
        if A[i] < 0:
            minus += 1
    if minus % 2 == 1:
        ans -= 2*min(abs(A))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N % 2 == 0:
        print(sum([abs(i) for i in A]))
    else:
        print(sum([abs(i) for i in A]) - 2 * min([abs(i) for i in A if i < 0]))

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [abs(i) for i in a]
    c = [i for i in a if i < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    if N % 2 == 0:
        ans = 0
        for a in A:
            ans += abs(a)
    else:
        ans = 0
        for a in A:
            ans += abs(a)
        ans -= 2 * abs(A[0])
    print(ans)

=======
Suggestion 10

def main():
    print("hello world!")
