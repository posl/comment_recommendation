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
        B[i] = max(0, B[i]-A[i])
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1]-B[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] -= min(a[i], b[i])
        ans += min(a[i+1], b[i])
        a[i+1] -= min(a[i+1], b[i])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                ans += A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
        else:
            ans += B[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= B[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        if A[i+1] <= B[i]:
            ans += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] <= B[i]:
            count += A[i]
            if A[i+1] <= B[i] - A[i]:
                count += A[i+1]
                A[i+1] = 0
            else:
                count += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
        else:
            count += B[i]
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    for i in range(N):
        if A[i] <= B[i]:
            result += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                result += A[i+1]
                B[i] -= A[i+1]
            else:
                result += B[i]
                A[i+1] -= B[i]
        else:
            result += B[i]

    print(result)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    kill = 0
    for i in range(N):
        kill += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        kill += min(A[i+1], B[i])
        A[i+1] -= min(A[i+1], B[i])

    print(kill)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(n):
        if a[i] <= b[i]:
            ans += a[i]
            b[i] -= a[i]
            if a[i+1] <= b[i]:
                ans += a[i+1]
                a[i+1] = 0
            else:
                ans += b[i]
                a[i+1] -= b[i]
        else:
            ans += b[i]
    
    print(ans)

=======
Suggestion 9

def problems135_c():
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
        if B[i] >= A[i + 1]:
            ans += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0
        else:
            ans += B[i]
            A[i + 1] -= B[i]
            B[i] = 0
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_kill = 0
    for i in range(n):
        if a[i] >= b[i]:
            max_kill += b[i]
        else:
            max_kill += a[i]
            b[i] -= a[i]
            if a[i+1] >= b[i]:
                max_kill += b[i]
                a[i+1] -= b[i]
            else:
                max_kill += a[i+1]
                a[i+1] = 0
    print(max_kill)
