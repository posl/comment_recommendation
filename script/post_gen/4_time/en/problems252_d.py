Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k]:
                    continue
                if a[i] == a[k]:
                    continue
                if a[k] < a[i] + a[j]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1, N):
                if A[j] == A[k]:
                    continue
                if A[i] == A[k]:
                    continue
                if A[i] + A[j] > A[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1,N):
                if A[j] == A[k]:
                    continue
                if A[k] > A[i] + A[j]:
                    break
                else:
                    cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k]:
                    continue
                if a[k] > a[i] + a[j]:
                    break
                ans += 1
    print(ans)

=======
Suggestion 5

def solve(n, a):
    ans = 0
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(n):
        ans += c[a[i]]
        c[a[i]] += b[a[i]]
        b[a[i]] += 1
    return ans

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a.reverse()

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    ans += 1

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    cnt = 0
    i = 0
    j = 1
    k = 2
    while i < N-2:
        if A[i] == A[i+1]:
            i += 1
            continue
        j = i+1
        while j < N-1:
            if A[j] == A[j+1]:
                j += 1
                continue
            k = j+1
            while k < N:
                if A[k] == A[k+1]:
                    k += 1
                    continue
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    cnt += 1
                k += 1
            j += 1
        i += 1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    cnt = 0
    prev = 0
    prev_cnt = 0
    for i in range(n):
        if prev != a[i]:
            cnt += prev_cnt * (prev_cnt - 1) // 2
            prev = a[i]
            prev_cnt = 1
        else:
            prev_cnt += 1
    print(cnt)

=======
Suggestion 9

def solve(n, a):
    from collections import Counter
    c = Counter(a)
    v = c.values()
    ans = 0
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            for k in range(j+1, len(v)):
                ans += v[i] * v[j] * v[k]
    return ans

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # 各要素の個数をカウント
    cnt = [0] * (10**5+1)
    for a in A:
        cnt[a] += 1

    # 2つの要素の組み合わせの個数をカウント
    cnt2 = [0] * (10**5+1)
    for i in range(10**5+1):
        cnt2[i] = cnt[i] * (cnt[i]-1) // 2

    # 3つの要素の組み合わせの個数をカウント
    cnt3 = [0] * (10**5+1)
    for i in range(10**5+1):
        for j in range(i+1, 10**5+1):
            cnt3[i] += cnt2[i] * cnt[j]

    # 3つの要素の組み合わせの個数を総和
    print(sum(cnt3))
