Synthesizing 10/10 solutions

=======
Suggestion 1

def check(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if check(L[i], L[j], L[k]) and L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                ans += 1

print(ans)

=======
Suggestion 2

def is_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

=======
Suggestion 3

def triangle():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[k] != sticks[i]:
                    if sticks[i] + sticks[j] > sticks[k]:
                        res += 1
    print(res)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] + a[j] > a[k] and a[i] != a[j] and a[j] != a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        cnt += 1
    print(cnt)

=======
Suggestion 6

def triangle_count():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    res = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    res += 1
    print(res)

triangle_count()

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def triangle():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def triangle_count(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    return ans

=======
Suggestion 10

def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k]:
                    count += 1
    return count
