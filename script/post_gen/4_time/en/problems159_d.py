Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    for a in A:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    sum = 0
    for k, v in dic.items():
        sum += v * (v-1) // 2
    for a in A:
        print(sum - (dic[a] - 1))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dic = {}
    for i in range(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    total = 0
    for key in dic:
        total += dic[key] * (dic[key] - 1) // 2
    for i in range(N):
        print(total - (dic[A[i]] - 1))

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    for i in range(n):
        print(ans - d[a[i]] + 1)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(1, N+1):
        d[i] = 0
    for i in range(N):
        d[A[i]] += 1
    ans = 0
    for i in range(1, N+1):
        ans += d[i]*(d[i]-1)//2
    for i in range(N):
        print(ans-(d[A[i]]-1))

=======
Suggestion 5

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(1, n + 1):
        print(ans - cnt[a[i]] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for a in A:
        ans[a - 1] += 1
    for a in ans:
        print(a)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]*(n+1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        ans += c[i]*(c[i]-1)//2

    for i in range(n):
        print(ans-c[a[i]]+1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    sum = 0
    for i in range(n):
        sum += b[i] * (b[i]-1) // 2
    for i in range(n):
        print(sum - b[a[i]-1] + 1)

=======
Suggestion 9

def solve(n, a):
    from collections import Counter
    c = Counter(a)
    ans = 0
    for k in range(1, n+1):
        ans += c[k] * (c[k] - 1) // 2
    for k in range(1, n+1):
        print(ans - (c[a[k-1]] - 1))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    #print(d)
    ans = 0
    for i in range(N):
        ans += d[A[i]] - 1
    for i in range(N):
        print(ans - d[A[i]] + 1)
