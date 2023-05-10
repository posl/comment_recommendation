Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 0
    min_diff = 100000000
    for i in range(N):
        tmp = T - H[i] * 0.006
        diff = abs(A - tmp)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1

    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = 100000000000000
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < diff:
            ans = i + 1
            diff = abs(a - temp)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [abs(a - (t - x * 0.006)) for x in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 4

def main():
  n = int(input())
  t, a = map(int, input().split())
  h = list(map(int, input().split()))
  ans = 0
  ans_diff = 1000000000
  for i in range(n):
    diff = abs(a-(t-h[i]*0.006))
    if ans_diff > diff:
      ans_diff = diff
      ans = i+1
  print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 0
    min_diff = 1000000000
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if min_diff > diff:
            min_diff = diff
            ans = i + 1

    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = float('inf')
    for i in range(n):
        tmp = abs(a - (t - h[i] * 0.006))
        if diff > tmp:
            ans = i + 1
            diff = tmp
    print(ans)

=======
Suggestion 7

def get_input():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    return N, T, A, H

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000
    ans = 0
    for i in range(n):
        if min > abs(a - (t - h[i] * 0.006)):
            min = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 9

def calc_temp(h, t):
    return t - h * 0.006

=======
Suggestion 10

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    diff = [abs(t - (t - h[i] * 0.006) - a) for i in range(n)]
    print(diff.index(min(diff)) + 1)
