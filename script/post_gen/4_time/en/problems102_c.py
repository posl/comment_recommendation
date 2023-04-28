Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 0:
        print(b[n // 2] - b[n // 2 - 1])
    else:
        print(b[n // 2] - b[n // 2])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i+1)
    b.sort()
    if n % 2 == 0:
        x = (b[n//2 - 1] + b[n//2]) // 2
    else:
        x = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i] - x)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = a[i] - (i+1)
    b.sort()
    if n % 2 == 0:
        b1 = b[n//2]
        b2 = b[n//2-1]
        ans = 0
        for i in range(n):
            ans += abs(b1-b[i])
            ans += abs(b2-b[i])
        ans = min(ans, ans2)
    else:
        b1 = b[n//2]
        ans = 0
        for i in range(n):
            ans += abs(b1-b[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    b = A[N//2]
    print(sum([abs(A[i] - b) for i in range(N)]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - i - 1 for i, a in enumerate(A)]
    A.sort()
    b = A[N // 2]
    ans = 0
    for a in A:
        ans += abs(a - b)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i]-(i+1) for i in range(N)]
    B.sort()
    if N%2 == 1:
        b = B[int(N/2)]
    else:
        b = (B[int(N/2)] + B[int(N/2-1)])/2
    print(int(sum([abs(A[i]-(b+(i+1))) for i in range(N)])))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - (i+1))
    b.sort()
    b1 = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i]-b1)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ave = sum/n
    ave = round(ave)
    sum = 0
    for i in range(n):
        sum += (a[i] - ave)**2
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    median = A[int(N/2)]
    sum = 0
    for i in range(N):
        sum += abs(A[i]-median)
    print(sum)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    A_sum_abs = sum(map(abs, A))
    A.sort()
    if N % 2 == 0:
        b = (A[N//2-1] + A[N//2]) // 2
        b2 = b + 1
        b1 = b - 1
        print(min(
            A_sum_abs - 2 * (A_sum - (b1 + 1) * N),
            A_sum_abs - 2 * (A_sum - (b2 + 1) * N)
        ))
    else:
        b = A[N//2]
        print(A_sum_abs - 2 * (A_sum - (b + 1) * N))
