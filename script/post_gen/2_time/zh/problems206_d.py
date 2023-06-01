Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(n * (n - 1) // 2 - ans)

=======
Suggestion 2

def main():
    n = int(input())
    if n < 2 or n > 3 * 10 ** 5:
        return
    a = list(map(int, input().split()))
    if len(a) != n:
        return
    # print(a)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # print(A)
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (10**9 + 1)
    for i in a:
        count[i] += 1
    ans = 0
    for i in range(10**9 + 1):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

=======
Suggestion 6

def solve(n, a):
    ans = 0
    cnt = [0] * (10 ** 6 + 1)
    for i in range(n):
        ans += i - cnt[a[i]]
        cnt[a[i]] += 1
    return ans

=======
Suggestion 7

def problem206_c():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(n * (n - 1) // 2 - ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0 for _ in range(10 ** 9 + 1)]
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(10 ** 9 + 1):
        ans += c[i] * (c[i] - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 10

def count_pairs(N, A):
    from collections import Counter
    counter = Counter(A)
    total = 0
    for v in counter.values():
        total += v * (v - 1) // 2
    return total
