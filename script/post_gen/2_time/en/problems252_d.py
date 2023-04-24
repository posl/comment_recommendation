Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            k = bisect.bisect_left(A, A[i]+A[j])
            ans += k-j-1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1, N):
                if A[j] == A[k]:
                    continue
                if A[i] + A[j] > A[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N - i) * (N - i + 1) // 2
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if A[i] > A[j]:
                ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, 10**5 + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) // 2
    for a in A:
        if cnt[a] >= 2:
            print(ans - (cnt[a] - 1))
        else:
            print(ans)

=======
Suggestion 8

def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    c = Counter(A)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if c[A[j]] > 1 or A[i] + A[j] > A[j+1]:
                ans += 1
    print(ans)
main()

=======
Suggestion 9

def  main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A.sort()
    ans = 0
    for i in range(1, N+1):
        ans += (i-1) * (N-i) * (A[i+1] - A[i-1])
    print(ans)
