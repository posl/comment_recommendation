Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                ans = max(ans, A[i] + A[j])
                break
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                return A[i] + A[j]
    return -1

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
    print(max_even)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    for i in range(N):
        for j in range(i + 1, N):
            if (A[i] + A[j]) % 2 == 0:
                print(A[i] + A[j])
                return
    print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = []
    for i in range(N):
        if A[i] % 2 == 0:
            even.append(A[i])
    if len(even) == 0:
        print(-1)
        exit()
    else:
        for i in range(1, len(even)):
            even[i] += even[i - 1]
    for i in range(N):
        if A[i] % 2 == 1:
            for j in range(len(even)):
                if A[i] + even[j] % 2 == 0:
                    print(A[i] + even[j])
                    exit()
    print(-1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    res = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                res = max(res, a[i] + a[j])
                break

    print(res)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in reversed(range(N)):
        for j in reversed(range(i)):
            if (A[i] + A[j]) % 2 == 0:
                return A[i] + A[j]
    return -1

print(solve())

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    even = []
    for i in range(n):
        if a[i] % 2 == 0:
            even.append(a[i])
    if len(even) == 0:
        print(-1)
        return
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return

main()

=======
Suggestion 9

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0 and a[i] + a[j] > max:
                max = a[i] + a[j]
    print(max)

solution()

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = Counter(A)
    max_A = A.most_common()[0][0]
    if max_A % 2 == 1:
        max_A -= 1
    for a in A:
        if a == max_A:
            continue
        if max_A - a in A:
            print(max_A)
            exit()
    print(-1)
