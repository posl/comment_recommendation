Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1] + 1:
            ans += 1
        elif a[i] <= a[i - 1]:
            ans += a[i]
        else:
            print(-1)
            return
    print(n - 1 - ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
            return
        else:
            print(-1)
            return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
            return
        elif a[0] == 2 and a[1] == 1:
            print(1)
            return
        else:
            print(-1)
            return
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] == i + 1:
            ans += 1
        else:
            print(-1)
            return
    print(n - ans)

=======
Suggestion 3

def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            ans += 1
    print(n - 1 - ans)
resolve()

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    print(N - ans if ans != N else -1)
main()

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n-1:
        print(1)
    elif ans == n-2:
        if a[0] == n and a[n-1] == 1:
            print(3)
        else:
            print(2)
    else:
        print(-1)

=======
Suggestion 7

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans)

=======
Suggestion 8

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  if n == 1:
    if a[0] == 1:
      print(0)
    else:
      print(-1)
    return
  if a[0] != 1:
    print(-1)
    return
  ans = 0
  for i in range(1, n):
    if a[i] - a[i - 1] > 1:
      print(-1)
      return
    elif a[i] - a[i - 1] == 1:
      ans += 1
  print(n - ans - 1)
  return

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    cnt = 0
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            cnt += 1
        elif a[i+1] == a[i]:
            cnt += 1
        elif a[i+1] - a[i] > 1:
            print(-1)
            return
    print(n - cnt - 1)
main()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        if B[i] > i + 1:
            ans += B[i] - (i + 1)
    print(ans)
