Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return n,a,b,c

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))

    count = [0] * n
    for i in range(n):
        count[b[c[i]]] += 1

    ans = 0
    for i in range(n):
        ans += count[a[i]]

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    d = [0] * n
    for i in range(n):
        d[b[c[i] - 1] - 1] += 1
    print(sum([d[a[i] - 1] for i in range(n)]))

=======
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * N
    for i in range(N):
        B_C[C[i]-1] += 1

    A_B_C = [0] * N
    for i in range(N):
        A_B_C[B[i]-1] += B_C[i]

    ans = 0
    for i in range(N):
        ans += A_B_C[A[i]-1]

    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * N
    for i, c in enumerate(C):
        B_C[c - 1] += 1

    A_B_C = [0] * N
    for i, b in enumerate(B):
        A_B_C[A[i] - 1] += B_C[i]

    print(sum(A_B_C))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    count = 0
    for i in range(N):
        count += B[C[i] - 1] == A[i]

    print(count)

=======
Suggestion 9

def findPairs(A, B, C):
    count = 0
    for i in range(len(A)):
        if A[i] == B[C[i] - 1]:
            count += 1
    return count
