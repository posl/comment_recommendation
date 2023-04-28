Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, (r - l + 1) * x)

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x * (j-i+1))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i,N):
            x = min(A[i:j+1])
            ans = max(ans, x*(j-i+1))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l,N):
            if x > A[r]:
                x = A[r]
            ans = max(ans, x*(r-l+1))
    print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            result = max(result, x * (j - i + 1))
    print(result)

=======
Suggestion 7

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a
