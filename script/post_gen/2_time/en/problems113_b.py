Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    avg_temp = [T - h * 0.006 for h in H]
    min_diff = float('inf')
    ans = 0
    for i, temp in enumerate(avg_temp, 1):
        diff = abs(temp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i

    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 1
    min_diff = abs(a - (t - h[0] * 0.006))
    for i in range(1, n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 100
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < diff:
            ans = i + 1
            diff = abs(T - H[i] * 0.006 - A)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    diff = 10**9
    ans = 0
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < diff:
            diff = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 1
    min_diff = abs(a - (t - h[0] * 0.006))
    for i in range(1, n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            ans = i + 1
            min_diff = diff

    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if abs(t - h[i] * 0.006 - a) < abs(t - h[ans - 1] * 0.006 - a):
            ans = i + 1
    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 10 ** 9
    for i in range(N):
        tmp = T - H[i] * 0.006
        diff = abs(tmp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = float("inf")
    for i, h in enumerate(H):
        temp = T - h * 0.006
        diff = abs(temp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = 100000000
    for i in range(n):
        if diff > abs(a - (t - h[i] * 0.006)):
            diff = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0
    min_diff = 10**9
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)
