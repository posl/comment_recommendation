Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if n % 2 == 0:
        a_m = (a[n // 2] + a[n // 2 - 1]) // 2
        b_m = (b[n // 2] + b[n // 2 - 1]) // 2
        print(b_m - a_m + 1)
    else:
        a_m = a[n // 2]
        b_m = b[n // 2]
        print(b_m - a_m + 1)

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
    min_time = 1000000
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[i])
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
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(min(max(a), max(b)))

=======
Suggestion 5

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**9 + 1
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 7

def solve():
    # Implement solution here
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min(max(A), max(B)))

=======
Suggestion 8

def min_time(N, A, B):
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    return min_time

=======
Suggestion 9

def solve():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab = sorted(ab, key=lambda x: x[0]+x[1])
    print(ab[-1][0]+ab[-1][1])

=======
Suggestion 10

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))

    #print(N)
    #print(AB)
    print(min([max(AB[i][0],AB[i][1]) for i in range(N)]))
