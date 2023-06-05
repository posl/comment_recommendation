Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a = list(set(a))
    n = len(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[k] < a[i] + a[j]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] == a[j]:
                continue
            for k in range(j+1,n):
                if a[i] == a[k] or a[j] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (200000 + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, 200000 + 1):
        if cnt[i] >= 3:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) * (N - cnt[i])
        for j in range(i + 1, 200000 + 1):
            if cnt[i] >= 1 and cnt[j] >= 2:
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
            if cnt[i] >= 2 and cnt[j] >= 1:
                ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[j]
            if cnt[i] >= 1 and cnt[j] >= 1:
                k = i + j
                if k <= 200000 and cnt[k] >= 1:
                    ans += cnt[i] * cnt[j] * cnt[k]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += bisect.bisect_left(a, a[i] + a[j]) - j - 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def f(n, a):
    c = [0] * (10**5+1)
    for i in a:
        c[i] += 1
    s = sum([i*(i-1)//2*(i-2)//3 for i in c])
    return s

n = int(input())
a = list(map(int, input().split()))
print(f(n, a))

=======
Suggestion 8

def solve():
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
                if A[k] > A[i] + A[j]:
                    break
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

=======
Suggestion 10

def three_trio():
    # 读取N
    N = int(input())
    # 读取A
    A = list(map(int, input().split(' ')))
    # 三联体数量
    trio = 0
    # A_i
    for i in range(N - 2):
        # A_j
        for j in range(i + 1, N - 1):
            # A_k
            for k in range(j + 1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    trio += 1
    return trio

print(three_trio())
