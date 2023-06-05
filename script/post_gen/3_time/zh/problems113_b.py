Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))

    temp = 100000
    index = 0
    for i in range(N):
        if abs(A - (T-H[i]*0.006)) < temp:
            temp = abs(A - (T-H[i]*0.006))
            index = i
    print(index+1)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    min = 1000000000
    index = 0
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(temp - a) < min:
            min = abs(temp - a)
            index = i + 1

    print(index)

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    min_diff = 1000
    index = 0
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            index = i + 1
    print(index)

=======
Suggestion 4

def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    h = [abs(T - H[i] * 0.006 - A) for i in range(N)]
    print(h.index(min(h)) + 1)

main()

=======
Suggestion 5

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [abs(a - (t - i * 0.006)) for i in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 6

def get_input():
    n = int(input())
    t, a = map(int, input().split())
    h_list = list(map(int, input().split()))
    return n, t, a, h_list

=======
Suggestion 7

def main():
    n = int(input())
    t, a = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    min = 100000000
    for i in range(0,n):
        if min > abs(a - (t - h[i] * 0.006)):
            min = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - x * 0.006 for x in h]
    h = [abs(a - x) for x in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 9

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    t -= a
    min = 100000000
    index = 0
    for i in range(n):
        if abs(t-h[i]*0.006) < min:
            min = abs(t-h[i]*0.006)
            index = i+1
    print(index)

=======
Suggestion 10

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min_diff = 1000000
    min_diff_idx = 0
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            min_diff = diff
            min_diff_idx = i + 1
    print(min_diff_idx)
