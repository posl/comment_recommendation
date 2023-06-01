Synthesizing 10/10 solutions

=======
Suggestion 1

def min_time(n, a, b):
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    return min_time

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
    ans = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i]+B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)
solve()

=======
Suggestion 3

def min_time(n,a,b):
    min_time = 0
    for i in range(n):
        if a[i] > b[i]:
            min_time += b[i]
        else:
            min_time += a[i]
    return min_time

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
    t = 0
    for i in range(N):
        t += A[i]
    ans = t
    for i in range(N):
        t = t - A[i] + B[i]
        if t > ans:
            ans = t
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

=======
Suggestion 7

def main():
    n = int(input())
    min_time = 10**5*2
    for i in range(n):
        a,b = map(int,input().split())
        if a+b < min_time:
            min_time = a+b
    print(min_time)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 10 ** 10
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, a[i] + b[j])
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

=======
Suggestion 10

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    if max(a) > max(b):
        print(max(a))
    else:
        print(max(b))
