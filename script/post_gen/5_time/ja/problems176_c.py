Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > A[i-1]:
            ans += A[i] - A[i-1]
    print(ans)
main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            print(-1)
            return
        elif A[i] < i + 1:
            ans += i + 1 - A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(A[i] - i)
    B.sort()
    #print(B)
    min = B[0]
    for i in range(1, N):
        if B[i] - B[i-1] < min:
            min = B[i] - B[i-1]
    #print(min)
    ans = 0
    for i in range(N):
        ans += A[i] - (B[i] - min)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += max(0,A[i]-A[i-1])
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1,n):
        if a[i] > a[i-1]:
            continue
        ans += a[i-1] - a[i]
        a[i] = a[i-1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    a.reverse()
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
            a[i] = a[i-1]
    print(ans)

=======
Suggestion 7

def solve(n, a):
    # ここに処理を追加してください
    #print(a)
    max = 0
    sum = 0
    for i in range(n-1):
        if a[i] > max:
            max = a[i]
        if a[i+1] < max:
            sum += max - a[i+1]
    return sum

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < ans:
            print(-1)
            return
        ans = max(ans, a[i])
        ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i
    ans = 0
    tmp = 0
    for i in range(N):
        if i == 0:
            tmp = B[i]
        else:
            if tmp > B[i]:
                ans += 1
            else:
                tmp = B[i]
    print(ans)

=======
Suggestion 10

def main():
  N = int(input())
  A = list(map(int, input().split()))
  ans = 0
  for i in range(N-1, -1, -1):
    if A[i] <= ans:
      ans = A[i]
    else:
      ans = A[i] - 1
  print(ans)
