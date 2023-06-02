Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, a[i]+b[j])
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

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
    min_time = 10**10
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
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if n % 2 == 0:
        a_median = (a[n // 2] + a[n // 2 - 1]) / 2
        b_median = (b[n // 2] + b[n // 2 - 1]) / 2
        print(int(b_median - a_median + 1))
    else:
        a_median = a[n // 2]
        b_median = b[n // 2]
        print(int(b_median - a_median + 1))

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
    min_time = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

=======
Suggestion 5

def min_time(a_list, b_list):
    min_time = 10**10
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if i == j:
                time = a_list[i] + b_list[j]
            else:
                time = max(a_list[i], b_list[j])
            if time < min_time:
                min_time = time
    return min_time

=======
Suggestion 6

def min_time(works):
    works.sort(key=lambda x: x[0] + x[1])
    return works[-1][0] + works[-2][1]

=======
Suggestion 7

def getMinTime(n, a, b):
    minTime = 0
    for i in range(n):
        minTime += min(a[i], b[i])
    return minTime

n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())

print(getMinTime(n, a, b))

=======
Suggestion 8

def solve():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]
    ans = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans,AB[i][0]+AB[j][1])
            else:
                ans = min(ans,max(AB[i][0],AB[j][1]))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

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
    min_time = float('inf')
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    return min_time

print(solve())
