Synthesizing 10/10 solutions

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
        for j in range(n):
            if a[i] == a[j]:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 2

def solve():
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
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] in d:
                ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if A[i]*A[j] == A[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if (A[i] / A[j]) == A[k]:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                for k in range(N):
                    if A[j] % A[k] == 0:
                        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if A[k] == A[i] // A[j]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans += 1
    else:
        for j in range(i + 1, n):
            if a[j] == a[i]:
                ans += 1
            elif a[j] % a[i] == 0:
                break
print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                for k in range(0, n):
                    if i != k and j != k:
                        if a[i] * a[k] == a[j]:
                            count += 1
    print(count//2)
