Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (max(a) + 1)
for i in a:
    cnt[i] += 1

ans = 0
for i in range(1, max(a) + 1):
    for j in range(i, max(a) + 1, i):
        if cnt[j] == 0:
            continue
        if i == j:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        elif i < j:
            k = gcd(i, j)
            if k == i:
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
            elif k == j:
                ans += cnt[i] * cnt[j] * (cnt[i] - 1) // 2
            else:
                ans += cnt[i] * cnt[j] * cnt[k]
print(ans)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if gcd(a[i], a[j]) == a[k] or gcd(a[j], a[k]) == a[i] or gcd(a[k], a[i]) == a[j]:
                cnt += 1
print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] > n:
                continue
            if a[a[i]//a[j]] == 0:
                continue
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n+1)
    c = [0] * (n+1)
    for i in range(1, n+1):
        b[a[i]] += 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            c[i * a[j]] += b[i]
    ans = 0
    for i in range(1, n+1):
        ans += c[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] % a[j] == 0:
                for k in range(j+1, n):
                    if a[j] % a[k] == 0:
                        count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (max(a)+1)
    for i in range(n):
        c[a[i]] += 1
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] <= max(a):
                s += c[a[i]*a[j]]
    print(s)

=======
Suggestion 7

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 8

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 9

def count_pairs(A):
    N = len(A)
    counter = {}
    for i in range(N):
        if A[i] in counter:
            counter[A[i]] += 1
        else:
            counter[A[i]] = 1
    return counter

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    dic = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i] % a[j] == 0:
                if a[i] // a[j] in dic:
                    cnt += dic[a[i] // a[j]]
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    print(cnt)
