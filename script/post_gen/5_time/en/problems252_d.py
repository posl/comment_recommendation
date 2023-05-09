Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:
                        count += 1
    print(count)

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
                if A[i] != A[j] and A[i] != A[k] and A[j] != A[k]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1,N):
                if A[i] == A[k] or A[j] == A[k]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, N + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (N - cnt[i])
    print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-2):
        if A[i] == A[i+1]:
            continue
        for j in range(i+1, N-1):
            if A[j] == A[j+1]:
                continue
            if A[i] + A[j] <= A[-1]:
                cnt += 1
            else:
                break
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i = 0
    while i < N-2:
        if A[i] == A[i+1]:
            i += 1
            continue
        j = i+1
        while j < N-1:
            if A[j] == A[j+1]:
                j += 1
                continue
            ans += N - (j+1)
            j += 1
        i += 1
    print(ans)

=======
Suggestion 8

def solve(n, a):
    from collections import Counter
    cnt = Counter(a)
    ans = 0
    for k, v in cnt.items():
        if v >= 3:
            ans += v * (v - 1) * (v - 2) // 6
        elif v == 2:
            ans += cnt[k + 1] + cnt[k - 1]
        else:
            ans += cnt[k + 1] + cnt[k + 2]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(len(set(A)) - (1 if len(set(A)) % 2 == 0 else 0))

=======
Suggestion 10

def problem():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print("N: ", N)

    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (A[i] != A[j] and A[j] != A[k] and A[k] != A[i]):
                    #print("i: ", A[i], " j: ", A[j], " k: ", A[k])
                    ans += 1
    print(ans)
