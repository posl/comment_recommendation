Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1
        else:
            continue
    print(cnt)
main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1

    for i in range(n-1):
        if a[i] == i+1:
            if a[i+1] == i+2:
                cnt += 1

    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a = [0] + a
    cnt = 0
    for i in range(1, n + 1):
        if a[a[i]] == i:
            cnt += 1

    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] < i+1:
            continue
        for j in range(i+1, N):
            if a[i] == j+1 and a[j] == i+1:
                cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    ans = 0
    for i in range(n-1):
        if b[i] > b[i+1]:
            ans += 1
    print(ans+1)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] <= i + 1:
            continue
        else:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < i+1:
            continue
        for j in range(i+1, a[i]+1):
            if j <= a[j-1]:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        if i <= A[i - 1] and A[A[i - 1] - 1] == i:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            continue
        for j in range(i + 1, A[i] + 1):
            if A[j - 1] <= i + 1:
                ans += 1
    print(ans)
main()
