Synthesizing 10/10 solutions

=======
Suggestion 1

def min_sadness(n, a):
    min_sadness = 0
    sum_a = sum(a)
    sum_b = 0
    for i in range(n):
        sum_b += a[i]
        min_sadness += abs(sum_a - sum_b)
    return min_sadness

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i]-(i+1)
    B.sort()
    b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i]-(b+i+1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] - (i+1))
    B.sort()
    if N % 2 == 0:
        b = (B[N//2] + B[N//2-1]) // 2
    else:
        b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

=======
Suggestion 4

def solve():
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
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(0, N):
        B[i] = A[i] - i - 1
    B.sort()
    b = B[N // 2]
    ans = 0
    for i in range(0, N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    for i in range(n):
        b += a[i] - i - 1
    b = b // n
    c = [b-1,b,b+1]
    ans = float('inf')
    for i in c:
        tmp = 0
        for j in range(n):
            tmp += abs(a[j] - (i+j+1))
        ans = min(ans,tmp)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(N)]
    A.sort()
    b = A[N // 2]
    print(sum([abs(A[i] - b) for i in range(N)]))

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    b = B[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)

solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = 0
    min = 10**9
    for i in range(-100, 101):
        b = i
        sum = 0
        for j in range(N):
            sum += abs(A[j] - (b+j+1))
        if sum < min:
            min = sum
    print(min)

=======
Suggestion 10

def func(n, A):
    b = 0
    min = 0
    for i in range(n):
        min += abs(A[i] - (b + i + 1))
    return min
