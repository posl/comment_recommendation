Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    N = int(input())
    T, A = map(int, input().split())
    Hs = list(map(int, input().split()))

    # compute
    diffs = []
    for H in Hs:
        diffs.append(abs(A - (T - H * 0.006)))

    # output
    print(diffs.index(min(diffs)) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 100000000
    min_diff_index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i + 1
    print(min_diff_index)

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 10000000
    min_index = 0
    for i in range(n):
        if abs(a - (t - h[i] * 0.006)) < min:
            min = abs(a - (t - h[i] * 0.006))
            min_index = i + 1
    print(min_index)

=======
Suggestion 4

def main():
    N = int(input())
    T, A = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]
    min_diff = 1000000000
    min_index = -1
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1
    print(min_index)

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_diff = 10000000
    min_diff_index = 0
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i + 1
    print(min_diff_index)

=======
Suggestion 6

def main():
    # Get input here
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    # Calculate result here
    min_diff = float('inf')
    min_index = 0
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1

    # Print result here
    print(min_index)

=======
Suggestion 7

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    closest = 100000000
    closest_index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < closest:
            closest = diff
            closest_index = i + 1
    print(closest_index)

=======
Suggestion 8

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 100000000000000
    min_diff_i = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_i = i
    print(min_diff_i + 1)

=======
Suggestion 9

def problem113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    t -= a
    ans = 0
    min_diff = 1e9
    for i in range(n):
        diff = abs(t - h[i] * 0.006)
        if diff < min_diff:
            ans = i + 1
            min_diff = diff
    print(ans)

=======
Suggestion 10

def average_temperature(t, x):
    return t - x * 0.006
