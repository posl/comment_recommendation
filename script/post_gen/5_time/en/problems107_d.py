Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(n):
        for j in range(i, n):
            m.append(sorted(a[i:j+1])[(j-i)//2])
    print(sorted(m)[len(m)//2])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    m = [0] * n
    m[0] = a[0]
    for i in range(1, n):
        m[i] = max(m[i - 1], a[i])
    for i in range(n):
        m[i] = max(m[i], (b[i] + m[i - 1]) / (i + 1))
    print(m[-1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i - 1
    b.sort()
    if n % 2 == 1:
        print(b[n // 2] + n // 2 + 1)
    else:
        print((b[n // 2] + b[n // 2 - 1]) // 2 + n // 2)

=======
Suggestion 4

def median(a):
    a.sort()
    if len(a) % 2 == 0:
        return (a[int(len(a)/2)-1] + a[int(len(a)/2)])/2
    else:
        return a[int(len(a)/2)]

n = int(input())
a = list(map(int,input().split()))
m = []
for i in range(n):
    for j in range(i,n):
        m.append(median(a[i:j+1]))
print(median(m))

=======
Suggestion 5

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

n = int(input())
a = list(map(int, input().split()))

m = []
for i in range(n):
    for j in range(i+1, n+1):
        m.append(median(a[i:j]))

print(median(m))

=======
Suggestion 6

def median(l):
    l.sort()
    if len(l) % 2 == 0:
        return (l[int(len(l)/2)] + l[int(len(l)/2) - 1]) / 2
    else:
        return l[int(len(l)/2)]

n = int(input())
a = list(map(int, input().split()))

m = []
for i in range(n):
    for j in range(i, n):
        m.append(median(a[i:j+1]))

print(int(median(m)))

=======
Suggestion 7

def median(a):
    a = sorted(a)
    return a[len(a)//2]

n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(median(a[i:j+1]))
print(median(m))

=======
Suggestion 8

def median(a):
    a.sort()
    if len(a)%2 == 0:
        return a[len(a)//2]
    else:
        return a[len(a)//2]

N = int(input())
a = list(map(int, input().split()))
b = []
for i in range(N):
    for j in range(i+1,N+1):
        b.append(median(a[i:j]))
print(median(b))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans += A[i:j+1]
    print(ans)

=======
Suggestion 10

def median(a):
    a.sort()
    return a[len(a)//2]

n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append(median(a[i:]))

print(median(b))
