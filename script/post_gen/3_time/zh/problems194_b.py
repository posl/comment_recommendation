Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)
solve()

=======
Suggestion 2

def solve():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

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
    t = 0
    for i in range(N):
        if t < A[i]:
            t = A[i]
        if t % B[i] != 0:
            t += B[i] - t % B[i]
    print(t)

=======
Suggestion 4

def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 5

def min_time(n, a, b):
    min_time = 0
    for i in range(n):
        if a[i] > b[i]:
            min_time += b[i]
        else:
            min_time += a[i]
    return min_time

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_time = 1000000
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i],B[j])
            if min_time > time:
                min_time = time
    print(min_time)

=======
Suggestion 7

def min_time():
    #N = int(input())
    N = 3
    #A = []
    #B = []
    #for i in range(N):
    #    A_i, B_i = map(int, input().split())
    #    A.append(A_i)
    #    B.append(B_i)
    A = [8, 4, 7]
    B = [5, 4, 9]
    min_time = 0
    for i in range(N):
        if A[i] > B[i]:
            min_time += A[i]
        else:
            min_time += B[i]
    print(min_time)

=======
Suggestion 8

def solution():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = float('inf')
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, a[i] + b[j])
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

=======
Suggestion 9

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i] + B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)

=======
Suggestion 10

def get_min(a, b):
    if a < b:
        return a
    else:
        return b
