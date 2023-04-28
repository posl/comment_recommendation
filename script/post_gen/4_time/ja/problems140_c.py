Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 2

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    print(sum(a))

=======
Suggestion 3

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(n-2):
        a.append(min(b[i], b[i+1]))
    a.append(b[-1])
    print(sum(a))

=======
Suggestion 4

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[1] = B[0]
    for i in range(1, N-1):
        A[i+1] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 5

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = []
    A.append(B[0])
    A.append(B[0])
    for i in range(1, N-1):
        A.append(min(B[i-1], B[i]))
    A.append(B[N-2])
    print(sum(A))

=======
Suggestion 6

def main():
    # input
    N = int(input())
    Bs = list(map(int, input().split()))

    # compute
    As = [0] * N
    As[0] = Bs[0]
    As[-1] = Bs[-1]
    for i in range(N-2):
        As[i+1] = min(Bs[i], Bs[i+1])
    # output
    print(sum(As))

=======
Suggestion 7

def main():
    N = int(input())
    B = list(map(int, input().strip().split()))
    A = [0] * N
    A[0] = B[0]
    A[N - 1] = B[N - 2]
    for i in range(N - 2):
        A[i + 1] = min(B[i], B[i + 1])
    print(sum(A))

=======
Suggestion 8

def solve():
    n = int(input())
    bs = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += min(bs[i], bs[i+1])
    ans += bs[0] + bs[-1]
    print(ans)

=======
Suggestion 9

def max_sum(n, b):
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    return sum(a)


n = int(input())
b = list(map(int, input().split()))
print(max_sum(n, b))
