Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    ans = 10 ** 18
    for i in xrange(-1, 2):
        b = a[n/2] + i
        tmp = 0
        for j in xrange(n):
            tmp += abs(a[j] - (b + j + 1))
        ans = min(ans, tmp)
    print ans

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    b = int(sum / n)
    c = b + 1
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += abs(a[i] - b)
        sum2 += abs(a[i] - c)
    print(min(sum1, sum2))

=======
Suggestion 3

def calcSadness(a, b):
    res = 0
    for i in range(len(a)):
        res += abs(a[i] - (b + i + 1))
    return res

n = int(input())
a = list(map(int, input().split()))
a.sort()
b = a[n // 2]
print(calcSadness(a, b))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - i - 1 for i in range(n)]
    a.sort()
    b = a[n // 2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    ans = 0
    for i in range(n):
        ans += abs(b[i] - b[n // 2])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    for i in range(N):
        b += A[i] - (i+1)
    b //= N
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)

=======
Suggestion 7

def problems102_c():
    pass

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(n):
        b.append(a[i]-i-1)
    b.sort()
    if n % 2 == 0:
        print(b[n//2]-b[n//2-1])
    else:
        print(b[n//2])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[i] - i - 1 for i in range(n)]
    b.sort()
    if n % 2 == 1:
        ans = sum([abs(b[n // 2] - b[i]) for i in range(n)])
    else:
        ans = min(sum([abs(b[n // 2] - b[i]) for i in range(n)]), sum([abs(b[n // 2 - 1] - b[i]) for i in range(n)]))
    print(ans)

=======
Suggestion 10

def calculate(A, b):
    sum = 0
    for i in range(0, len(A)):
        sum += abs(A[i] - (b + i + 1))
    return sum

N = int(input())
A = list(map(int, input().split()))
A.sort()
b = A[N//2]
print(calculate(A, b))
