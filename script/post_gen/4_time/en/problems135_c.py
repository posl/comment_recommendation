Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        ans += min(A[i+1], B[i])
        A[i+1] -= min(A[i+1], B[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        A[i] -= min(A[i], B[i])
        B[i] -= min(A[i-1], B[i])
        ans += min(A[i], B[i])
    print(ans)

main()

I made a mistake in the problem statement. I'm sorry for the inconvenience.

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if B[i] >= A[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if B[i] >= A[i+1]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if B[i] >= A[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
            if B[i] >= A[i+1]:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] >= B[i]:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
            else:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        if A[i+1] > B[i]:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
        else:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        ans += min(B[i], A[i])
        A[i] -= min(B[i], A[i])
        ans += min(B[i], A[i+1])
        A[i+1] -= min(B[i], A[i+1])
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
            if a[i+1] <= b[i]:
                ans += a[i+1]
                a[i+1] = 0
            else:
                ans += b[i]
                a[i+1] -= b[i]
        else:
            ans += b[i]
            a[i] -= b[i]
    print(ans)

solve()

I solved this problem on 2019/05/25.

=======
Suggestion 9

def solve(n, a, b):
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i + 1], b[i])
        a[i + 1] -= min(a[i + 1], b[i])
    ans += min(a[n], b[n - 1])
    return ans

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(solve(n, a, b))

=======
Suggestion 10

def solve(N,A,B):
    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] >= B[i]:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
            else:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
    return ans

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(solve(N,A,B))
