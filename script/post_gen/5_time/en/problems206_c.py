Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ret = 0
    for a in d:
        ret += d[a] * (d[a] - 1) // 2
    print(ret)

=======
Suggestion 2

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # compute

    # output
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    sum = 0
    for k in d:
        sum += d[k] * (d[k] - 1) // 2
    print(sum)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        ans += (j - i) * (N - j)
        i = j
    print(ans)

solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        cnt += (j - i) * (N - j)
        i = j
    print(cnt)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans += (N-i-1)*cnt
            cnt = 1
    print(ans)
    return 0

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += N - i - A.count(A[i])
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n - i - 1) - a[::-1].index(a[i])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        count += N - bisect_left(A, A[i]) - 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(1, n):
        count += i - a[i-1]
        if a[i] == a[i-1]:
            count += 1
    print(count)
