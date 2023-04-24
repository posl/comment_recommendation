Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2
    print(ans % 1000000007)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (A[i] + B[i]) * (B[i] - A[i] + 1) // 2
    print(ans % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        ans += (A[i] + B[i]) * (B[i] - A[i] + 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2

    print(ans % (10**9 + 7))

=======
Suggestion 5

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2
    print(ans % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(sum(B) - sum(A) + N)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(0, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(0, N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2

    print(int(ans))

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    sum = 0
    for i in range(N):
        sum += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2

    print(int(sum))

=======
Suggestion 9

def main():
    n = int(input())
    a = [0] * 1000000
    for i in range(n):
        s, t = map(int, input().split())
        a[s - 1] += 1
        a[t] -= 1
    for i in range(1, 1000000):
        a[i] += a[i - 1]
    print(sum(a))
