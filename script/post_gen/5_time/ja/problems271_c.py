Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    a.append(0)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            if cnt >= a[i]:
                ans += a[i]
            else:
                ans += cnt
            cnt = 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(N):
        if A[i] <= ans:
            ans += A[i]
        else:
            break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            exit()
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    cnt = 0
    for i in range(N):
        if cnt >= N-1:
            break
        if a[i] == a[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= ans + 1:
            ans += a[i]
        else:
            break
    print(ans + 1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] <= ans+1:
            ans += A[i]
        else:
            break
    print(ans+1)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > ans + 1:
            break
        else:
            ans += A[i]
    print(ans + 1)

=======
Suggestion 8

def calc():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            ans += 1
            break
    print(ans)

calc()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        ans *= a[i] - i
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= ans + 1:
            ans += a[i]
    print(ans + 1)
