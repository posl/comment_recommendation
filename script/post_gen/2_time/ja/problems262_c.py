Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        if a[i-1] == i:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        if a[i - 1] < i:
            continue
        for j in range(i + 1, n + 1):
            if a[j - 1] < j:
                continue
            if a[i - 1] == i and a[j - 1] == j:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= i + 1:
            ans += a[i] - (i + 1)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        ans += i * (i - 1) // 2
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, n + 1):
        ans -= c[i] * (c[i] - 1) // 2
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > i+1:
            continue
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (n + 1)
    for i, v in enumerate(a):
        l[v] = i + 1
    r = 0
    m = n + 1
    for i in range(n, 0, -1):
        if l[i] < m:
            r += 1
        m = min(m, l[i])
    print(r)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if min(A[i], A[j]) == i+1 and max(A[i], A[j]) == j+1:
                result += 1
    print(result)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] < i+1:
            continue
        ans += a[i] - (i+1)
    print(ans)
main()

=======
Suggestion 9

def main():
  N = int(input())
  A = list(map(int, input().split()))
  #print(N, A)

  count = 0
  for i in range(1, N+1):
    if A[i-1] >= i:
      count += 1
  print(count)
