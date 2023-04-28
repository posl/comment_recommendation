Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k]:
                        count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i]+l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))

    count = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                        count += 1

    print(count)

=======
Suggestion 8

def solve(n, L):
    L.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    return ans

=======
Suggestion 9

def check(a,b,c):
    if a < b + c and b < c + a and c < a + b:
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
            if check(L[i], L[j], L[k]):
                ans += 1

print(ans)

=======
Suggestion 10

def checkTriangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if checkTriangle(a[i], a[j], a[k]) and a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                ans += 1
print(ans)
