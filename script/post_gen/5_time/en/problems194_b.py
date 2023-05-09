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
    total = []
    for i in range(n):
        for j in range(n):
            if i == j:
                total.append(a[i] + b[j])
            else:
                total.append(max(a[i], b[j]))
    print(min(total))

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
    min_time = 10 ** 10
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
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = [int(x) for x in input().split()]
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    print(max(a[-1], b[-1]))

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    print(max(a[-1], b[-1]))

=======
Suggestion 6

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 10 ** 18
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)
solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if max_a < max_b:
        print(max_a)
    else:
        print(max_b)

=======
Suggestion 8

def main():
    #input
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #process
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[i]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    #output
    print(min_time)

=======
Suggestion 9

def min_time():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    return min(max(min(a), max(b)), max(min(b), max(a)))

print(min_time())

=======
Suggestion 10

def main():
    # Get the number of employees
    n = int(input())

    # Get the time taken by each employee to finish the two tasks
    times = []
    for i in range(n):
        times.append(list(map(int, input().split())))

    # Get the minimum time taken to finish the two tasks
    min_time = float('inf')
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, times[i][0] + times[j][1])
            else:
                min_time = min(min_time, max(times[i][0], times[j][1]))

    # Print the minimum time taken to finish the two tasks
    print(min_time)
