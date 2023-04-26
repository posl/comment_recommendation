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
            ans = max(ans, x * (r - l + 1))
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
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))
    print(ans)
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, x*(j-i+1))
    print(ans)

=======
Suggestion 6

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # compute
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, (j-i+1)*x)

    # output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_orange = 0
    for i in range(N):
        for j in range(i, N):
            x = 10**9
            for k in range(i, j+1):
                x = min(x, A[k])
            max_orange = max(max_orange, x*(j-i+1))
    print(max_orange)
