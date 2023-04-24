Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if j == k:
                    continue
                if A[j] % A[k] != 0:
                    continue
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                if a[i] // a[j] in d:
                    ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] * a[j] in a:
                cnt += 1
    print(cnt)

=======
Suggestion 5

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if j == k:
                    continue
                if A[j] * A[k] == A[i]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def solve(n, a):
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] != 0:
                continue
            for k in range(1, N+1):
                if A[i] == A[k]:
                    continue
                if A[j] == A[k]:
                    continue
                if A[i] / A[j] == A[k]:
                    count += 1
    print(count//2)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i]/a[j] == a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))

gcd_a = [a[0]]
for i in range(1,n):
    gcd_a.append(gcd(gcd_a[i-1], a[i]))

ans = 0
for i in range(n-1):
    if gcd_a[i] == a[i]:
        ans += 1
print(ans+n)
