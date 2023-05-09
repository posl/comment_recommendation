Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
        d[a[i]] -= 1
        for j in range(1, 200001):
            if a[i] % j == 0 and (a[i] // j) in d:
                ans += d[a[i] // j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i]*A[k] == A[j]*A[j]:
                    cnt += 1
                    if A[i]*A[j] == A[k]*A[k]:
                        cnt += 1
    print(cnt)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            k = A[i] * A[j]
            if k in d:
                ans += d[k]
    print(ans // 2)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i]*A[k] == A[j]**2:
                    cnt += 1
                if A[j]*A[k] == A[i]**2:
                    cnt += 1
    print(cnt)
    return 0

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i] * A[j] == A[k]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] * A[j] == A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [6, 2, 3]
    # N = 3
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]] += 1
        else:
            D[A[i]] = 1
    # print(D)
    # D = {6: 1, 2: 1, 3: 1}
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0 and A[i] // A[j] in D:
                ans += D[A[i] // A[j]]
    print(ans)
