Synthesizing 6/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        count += b[c[i]-1] == a[i]
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * N
    for i in range(N):
        B_C[C[i] - 1] += 1

    ans = 0
    for i in range(N):
        ans += B_C[B[A[i] - 1] - 1]

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    count = 0
    for i in range(n):
        a = A[i]
        b = B[i]
        c = C[i]
        count += B.index(a) * (n - C.index(a))

    print(count)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #print(N)
    #print(A)
    #print(B)
    #print(C)

    cnt = 0
    for i in range(N):
        cnt += B[C[i]-1] == A[i]

    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b_c = [0] * n

    for i in range(n):
        b_c[c[i]-1] += 1

    sum = 0
    for i in range(n):
        sum += b_c[b[a[i]-1]-1]

    print(sum)

=======
Suggestion 6

def solve(n, a, b, c):
    from collections import Counter
    a = Counter(a)
    b = Counter(b)
    c = Counter(c)
    c = [b[c[i]] for i in range(n)]
    return sum([a[i]*c[i] for i in range(n)])
