Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = [A[i], i]
    B.sort()
    ans = [K // N] * N
    K %= N
    for i in range(K):
        ans[B[i][1]] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    for i in range(N):
        if A[i] <= K % N:
            ans[i] -= 1
    print(*ans, sep="\n")

solve()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = K // N
    m = K % N
    for i in range(N):
        if i < m:
            print(k + 1)
        else:
            print(k)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    cnt = k // n
    k %= n
    for i in range(n):
        ans[i] = cnt
    b = sorted(a)
    for i in range(k):
        ans[b[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] += k // n
    for i in range(n):
        ans[i] -= k // n
    k %= n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k >= n:
        for i in range(n):
            print(k // n)
    else:
        b = [0 for i in range(n)]
        for i in range(k):
            b[i] = 1
        for i in range(n):
            print(b[a[i] - 1])

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n):
        ans[i] = k//n
    k %= n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[a[i]-1])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)

    ans = [0] * N
    cnt = 0
    for i in range(N):
        cnt += 1
        ans[i] = K // cnt
        if i == N - 1:
            break
        if K // cnt < K // (cnt + 1):
            K -= (K // cnt) * cnt
            for j in range(i + 1):
                ans[j] += K // (i + 1)
            K -= (K // (i + 1)) * (i + 1)

    for i in range(N):
        print(ans[A.index(A[i])])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    A_sorted_set = set(A_sorted)
    A_sorted_dict = {}
    for i, a in enumerate(A_sorted_set):
        A_sorted_dict[a] = i
    A_sorted_dict_rev = {}
    for k, v in A_sorted_dict.items():
        A_sorted_dict_rev[v] = k
    A_sorted_dict_rev_sorted = sorted(A_sorted_dict_rev.items(), key=lambda x:x[0])
    A_sorted_dict_rev_sorted_dict = {}
    for i, (k, v) in enumerate(A_sorted_dict_rev_sorted):
        A_sorted_dict_rev_sorted_dict[k] = v
    for i in range(N):
        print(K//N, flush=True)
        if K//N > 0:
            K -= K//N
        else:
            K = 0
        if K == 0:
            break
    if K == 0:
        return
    for i in range(K):
        print(A_sorted_dict_rev_sorted_dict[i]+1, flush=True)

=======
Suggestion 10

def calc(n, k, a):
    if k >= n:
        return [k//n]*n
    else:
        a.sort()
        r = [0]*n
        for i in range(k):
            r[a[i]-1] += 1
        return r
