Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] != i+1:
            cnt += 1
    if cnt > 2:
        print(-1)
    else:
        print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    B.sort(reverse=True)
    print(N - sum(B[:B.index(0)]))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    ans = 0
    for i in range(N):
        if A[i] != i + 1:
            ans += 1
    if ans == N:
        ans = -1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i+1 != a[i]:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    if n == 1:
        print(0)
        return
    for i in range(n-1):
        if a[i+1] - a[i] != 1:
            print(i+1)
            return
    print(-1)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] != i + 1:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1] + 1:
            pass
        elif A[i] == A[i-1]:
            ans += 1
        else:
            print(-1)
            return
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * N
    for i in range(N):
        b[a[i]] += 1
    for i in range(N):
        if b[i] > i + 1:
            print(-1)
            return
    print(N - sum(b))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != 1:
        print(-1)
        return

    ans = 0
    for i in range(n - 1):
        if a[i + 1] != a[i] + 1:
            ans += 1

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
            A[i+1] = A[i]
    if A[-1] == N:
        ans += 1
    print(N-ans)
