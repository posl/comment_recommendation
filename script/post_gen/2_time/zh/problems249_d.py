Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0
    for i in range(N):
        for j in range(N):
            if A[j] == 0:
                continue
            if A[i] % A[j] != 0:
                continue
            k = A[i] // A[j]
            if A.count(k) == 0:
                continue
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] * A[j] > A[N - 1]:
                break
            elif A[i] * A[j] in A:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0 for i in range(200001)]
    c = [0 for i in range(200001)]
    for i in range(1, n+1):
        b[a[i]] += 1
    for i in range(1, 200001):
        if b[i] > 0:
            for j in range(i, 200001, i):
                c[j] += b[i]
            if b[i] > 1:
                c[i] -= b[i]
    ans = 0
    for i in range(1, n+1):
        ans += c[a[i]]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    #print(A)

    # 1. A[i] / A[j] = A[k]
    # 2. A[i] / A[k] = A[j]
    # 3. A[j] / A[i] = A[k]
    # 4. A[j] / A[k] = A[i]
    # 5. A[k] / A[i] = A[j]
    # 6. A[k] / A[j] = A[i]

    # 1. A[i] = A[k] * A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] * A[j]
    # 6. A[k] = A[j] / A[i]

    # 1. A[i] * A[j] = A[k]
    # 2. A[i] / A[j] = A[k]
    # 3. A[j] * A[k] = A[i]
    # 4. A[j] / A[k] = A[i]
    # 5. A[k] * A[i] = A[j]
    # 6. A[k] / A[i] = A[j]

    # 1. A[i] = A[k] - A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] + A[j]
    # 6. A[k] = A[j] - A[i]

    # 1. A[i] = A[k] * A[j]
    # 2. A[i] = A[j] / A[k]
    # 3. A[j] = A[i] * A[k]
    # 4. A[j] = A[k] / A[i]
    # 5. A[k] = A[i] + A[j]
    #

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                cnt += d[a[i] // a[j]]
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 8

def solve(N, A):
    dic = {}
    for i in range(N):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0:
                if A[i] // A[j] in dic:
                    ans += dic[A[i] // A[j]]
    return ans

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0 for _ in range(max(a) + 1)]
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(1, max(a) + 1):
        for j in range(1, max(a) + 1):
            if i % j == 0:
                if i // j <= max(a):
                    ans += cnt[i] * cnt[j] * cnt[i // j]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] == 0 and A[j] == 0:
                continue
            if A[i] == 0 or A[j] == 0:
                continue
            if A[i] % A[j] == 0:
                cnt += 1
    print(cnt)
