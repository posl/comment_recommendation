Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,t,a)
    #print(n,t)

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    while t > 0:
        for i in range(n):
            if t >= a[i]:
                t -= a[i]
            else:
                print(i+1, t)
                exit()
    print(1, 0)

=======
Suggestion 3

def getSong(T, A, N):
    total = sum(A)
    T = T % total
    i = 0
    while T > 0:
        T = T - A[i]
        i += 1
    return i, T + A[i - 1]

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T - 1

    T = T % sum(A)
    for i in range(N):
        T = T - A[i]
        if T < 0:
            print(i + 1, -T)
            break

=======
Suggestion 5

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    t = t % sum(a)
    sum_a = 0
    for i in range(n):
        sum_a += a[i]
        if sum_a > t:
            print(i+1,t)
            break

=======
Suggestion 6

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    T = T % sumA
    for i in range(N):
        if A[i] > T:
            print(i+1, T)
            break
        T -= A[i]

solve()

=======
Suggestion 7

def solve():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    t %= sum(a)
    for i in range(n):
        if t<a[i]:
            print(i+1,t)
            break
        t -= a[i]
solve()

=======
Suggestion 8

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T %= sum(A)
    for i in range(N):
        if T < A[i]:
            print(i+1, T+1)
            break
        T -= A[i]

solve()

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve(n, t, a):
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            return i + 1, t
        t -= a[i]
