Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                if A[i] // A[j] in d:
                    ans += d[A[i] // A[j]]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                if A[i] * A[k] == A[j] * A[j]:
                    ans += 1
    print(ans // 2)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    for i in range(n):
        print(ans - (d[a[i]] - 1))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                if A[i] * A[k] == A[j]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] * A[k] == A[j] * A[j]:
                    cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] * a[j] == a[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j, A[i], A[j])
            if A[i] % A[j] == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
a.sort()
a_max = a[-1]
a_min = a[0]
a_gcd = a[0]
for i in range(1, n):
    a_gcd = gcd(a_gcd, a[i])

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            continue
        B.append(A[i])
    A = B
    N = len(A)
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if A[i] // A[j] == A[k]:
                    ans += 1
    print(ans)
