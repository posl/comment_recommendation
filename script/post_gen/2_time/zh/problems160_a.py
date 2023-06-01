Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] += 1
    ans = 0
    for i in range(n):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        print(ans - (b[a[i] - 1] - 1))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    from collections import Counter
    c = Counter(a)
    ans = [0] * n
    for k, v in c.items():
        ans[k-1] = v * (v-1) // 2
    for i in a:
        print(sum(ans) - ans[i-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = [0] * N
    for a in A:
        ans[a-1] = N - d[a]
    for a in ans:
        print(a)

=======
Suggestion 4

def solve():
    import sys

    f = open('problems159_d.txt', 'r')
    sys.stdin = f

    N = int(input())
    A = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += 1

    ans = 0
    for k in range(1, N+1):
        ans += d[k] * (d[k] - 1) // 2

    for i in range(N):
        print(ans - (d[A[i]] - 1))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += c[i] * (c[i] - 1) // 2
    for i in range(n):
        print(ans - c[a[i]] + 1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(n):
        print(ans - cnt[a[i]] + 1)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = {}
    for i in A:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    total = 0
    for i in count.values():
        total += i * (i - 1) // 2
    for i in A:
        print(total - (count[i] - 1))

=======
Suggestion 9

def count_pairs(n, a):
    cnt = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            if a[i-1] == a[j-1]:
                cnt += 1
    return cnt

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print("N = ", N)
    #print("A = ", A)
    ans = 0
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[A[i]] += 1
    #print("cnt = ", cnt)
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    #print("ans = ", ans)
    for i in range(N):
        print(ans - (cnt[A[i]] - 1))
    return
