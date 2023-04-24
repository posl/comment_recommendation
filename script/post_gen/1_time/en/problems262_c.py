Synthesizing 10/10 solutions

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
    b = [0] * (n+1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i - 1] == i:
            ans += 1
            a[i] = a[i - 1]
    if a[n - 1] == n:
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    minA = [0] * N
    maxA = [0] * N
    for i in range(N):
        minA[i] = i + 1
        maxA[i] = i + 1
    for i in range(N):
        if minA[A[i] - 1] > i + 1:
            minA[A[i] - 1] = i + 1
        if maxA[A[i] - 1] < i + 1:
            maxA[A[i] - 1] = i + 1
    ans = 0
    for i in range(N):
        if minA[i] == i + 1 and maxA[i] == i + 1:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N):
        if A[i] == i+1:
            cnt += 1
            A[i], A[i-1] = A[i-1], A[i]
        elif A[i-1] == i+1:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            if i + 1 < N and A[i + 1] == i + 2:
                ans += 1
            else:
                ans += 1
                break
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] >= i+1:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)

    #A = [0] + A
    #print(A)
    cnt = 0
    for i in range(1,N+1):
        if A[i-1] == i:
            if i == N:
                cnt += 1
            elif A[i] == i + 1:
                cnt += 1
        #print(i,cnt)
    print(cnt)

=======
Suggestion 10

def f(a):
    n = len(a)
    s = [0] * (n + 2)
    for i in range(n):
        s[a[i]] = i + 1
    s[n + 1] = 10**6
    res = 0
    for i in range(1, n + 1):
        if s[i] == i:
            x = s[i + 1]
            while x < n + 1 and s[x] == x:
                x += 1
            res += x - i
    return res

n = int(input())
a = [int(x) for x in input().split()]
print(f(a))
