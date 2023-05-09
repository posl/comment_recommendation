Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    for i in range(1, n):
        b[i] = 2 * a[i-1] - b[i-1]
    print(*b)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n

    for i in range(n):
        if i % 2 == 0:
            ans[0] += a[i]
        else:
            ans[0] -= a[i]

    for i in range(1, n):
        ans[i] = 2 * a[i - 1] - ans[i - 1]

    print(" ".join(map(str, ans)))

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = sum(a) - sum(a[1::2]) * 2
    for i in range(1, n):
        ans[i] = a[i - 1] * 2 - ans[i - 1]
    print(*ans)

=======
Suggestion 4

def compute():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i % 2 == 0:
            ans[0] += A[i]
        else:
            ans[0] -= A[i]
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    return " ".join(map(str, ans))

print(compute())

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = 0
    for i in range(n):
        t += a[i]
        if i % 2 == 0:
            print(t * 2 - s, end=' ')
        else:
            print(s - t * 2, end=' ')
    print()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    for i in range(1, n):
        x ^= a[i]
    x ^= a[0]
    print(*[x^a[i] for i in range(n)])

=======
Suggestion 7

def solve():
  n = int(input())
  a = [int(x) for x in input().split()]
  s = sum(a)
  ans = [0] * n
  ans[0] = s
  for i in range(1,n):
    ans[i] = 2 * (a[i-1] - ans[i-1] // 2)
  print(*ans)
solve()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    for i in range(n):
        k ^= a[i]
    for i in range(n):
        print(a[i] ^ k, end=' ')

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    for i in range(N):
        print(s-2*A[i], end=" ")
    print()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #print(N)
    #print(A)

    # 計算量が多すぎる
    #for i in range(N):
    #    for j in range(N):
    #        if j == 0:
    #            A[j] = A[j] - A[N-1]
    #        else:
    #            A[j] = A[j] - A[j-1]
    #    #print(A)

    # 計算量が多すぎる
    #for i in range(N):
    #    if i == 0:
    #        A[i] = A[i] - A[N-1]
    #    else:
    #        A[i] = A[i] - A[i-1]
    #print(A)

    # 計算量が多すぎる
    #for i in range(N):
    #    if i == 0:
    #        A[i] = A[i] - A[N-1]
    #    else:
    #        A[i] = A[i] - A[i-1]
    #    if i == N-1:
    #        print(A[i])
    #    else:
    #        print(A[i], end=' ')

    # 計算量が多すぎる
    #for i in range(N):
    #    if i == 0:
    #        A[i] = A[i] - A[N-1]
    #    else:
    #        A[i] = A[i] - A[i-1]
    #    print(A[i], end=' ')
    #print()

    # 計算量が多すぎる
    #for i in range(N):
    #    if i == 0:
    #        A[i] = A[i] - A[N-1]
    #    else:
    #        A[i] = A[i] - A[i-1]
    #    if i == N-1:
    #        print(A[i])
    #    else:
    #        print(A[i], end=' ')

    # 計算量が多すぎる
    #B = A
    #for i in range(N):
    #    if
