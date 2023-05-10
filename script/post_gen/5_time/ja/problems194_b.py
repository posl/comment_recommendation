Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        line = input().split(" ")
        A.append(int(line[0]))
        B.append(int(line[1]))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = max(ans, A[i] + B[j])
            else:
                ans = max(ans, max(A[i], B[j]))
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    print(min(max(a), max(b)))

=======
Suggestion 5

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
        ans = max(ans, A[i] + B[i])
    print(ans)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(min(max(a), max(b)))
    return 0

=======
Suggestion 8

def solve(n, a, b):
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    return ans

n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
print(solve(n, a, b))

=======
Suggestion 9

def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a = [x[0] for x in ab]
    b = [x[1] for x in ab]
    a.sort()
    b.sort()
    print(max(a[-1], b[-1]))

=======
Suggestion 10

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i] + B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)
