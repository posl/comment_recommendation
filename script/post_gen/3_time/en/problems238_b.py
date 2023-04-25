Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = 360 - ans
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    angle = 0
    for i in range(n):
        angle += a[i]
        angle %= 360
    print((360 - angle) % 360)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i]
    print(360 - s)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 360
    for i in range(N):
        ans = min(ans, abs(360 - 2 * (sum(A[i:]) % 360)))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = 360
    for i in range(N):
        X = min(X, abs(X-A[i]))
    print(X)

=======
Suggestion 6

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    A.append(360)
    A.append(0)
    A.rever

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - a for a in A]
    A = A[::-1]
    A.append(0)
    ans = 0
    for i in range(N + 1):
        ans += min(A[i], A[i + 1])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [360 - x for x in A]
    A.sort()
    A.append(360 + A[0])
    ans = 360
    for i in range(N):
        ans = min(ans, A[i + 1] - A[i])
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    upper = 180
    lower = 0
    for i in range(n):
        if a[i] <= upper and a[i] >= lower:
            upper = a[i] + 180
            lower = a[i]
        elif a[i] > upper:
            upper = upper + 360 - a[i]
            lower = a[i] - 180
        else:
            upper = a[i] + 180
            lower = lower - 360 + a[i]
    print(upper - 180)
