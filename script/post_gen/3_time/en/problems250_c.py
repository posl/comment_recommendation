Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input()) - 1
        A[x], A[x+1] = A[x+1], A[x]
    print(*A)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    ans = list(range(1, n+1))
    for i in range(q-1, -1, -1):
        tmp = ans[x[i]-1]
        ans[x[i]-1] = ans[x[i]]
        ans[x[i]] = tmp
    print(*ans)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    x = [int(input()) for i in range(q)]
    a = list(range(1, n + 1))
    for i in range(q):
        a[x[i] - 1], a[x[i]] = a[x[i]], a[x[i] - 1]
    print(*a)

=======
Suggestion 4

def solve():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    A = [i + 1 for i in range(N)]
    for i in range(Q):
        A[X[i] - 1], A[X[i]] = A[X[i]], A[X[i] - 1]
    print(*A)

=======
Suggestion 5

def swap(array, index):
    tmp = array[index]
    array[index] = array[index+1]
    array[index+1] = tmp

=======
Suggestion 6

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]
    return l

=======
Suggestion 7

def swap(i):
    global ball
    tmp = ball[i]
    ball[i] = ball[i + 1]
    ball[i + 1] = tmp

n, q = map(int, input().split())
ball = [i + 1 for i in range(n)]
for i in range(q):
    x = int(input())
    for j in range(n):
        if ball[j] == x:
            swap(j)
            break
    print(' '.join(map(str, ball)))

=======
Suggestion 8

def swap_balls(ball, x):
    if ball == x:
        return x
    elif ball == x-1:
        return x-1
    else:
        return ball

=======
Suggestion 9

def swap(x):
    global arr
    global arr2
    global n
    global m
    global count
    global flag
    global flag2
    if flag == 0:
        arr2[x-1],arr2[x] = arr2[x],arr2[x-1]
        if arr2[x-1] == x-1:
            flag = 1
        if flag2 == 1:
            count += 1
        if count == m:
            flag2 = 0
            count = 0
    else:
        arr2[x-1],arr2[x] = arr2[x],arr2[x-1]
        if arr2[x] == x:
            flag = 0
        if flag2 == 1:
            count += 1
        if count == m:
            flag2 = 0
            count = 0
    return arr2
n,m = map(int,input().split())
arr = list(range(n))
arr2 = list(range(n))
count = 0
flag = 0
flag2 = 1
for i in range(m):
    x = int(input())
    arr2 = swap(x)
print(*arr2)

=======
Suggestion 10

def swap(x, y):
    return y, x
