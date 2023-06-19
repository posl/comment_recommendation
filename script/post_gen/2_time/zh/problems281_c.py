Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    
    t = t % sum(a)
    
    for i in range(n):
        if t < a[i]:
            break
        t -= a[i]
    print(i+1,t)

=======
Suggestion 2

def play_list():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    t %= sum(a)
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i + 1, -t)
            break

=======
Suggestion 3

def problem281_c():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    t = t%n
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1,t)
            break
    return

problem281_c()

=======
Suggestion 4

def play_list():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i + 1, -T)
            break
play_list()

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    s = sum(A)
    T = T % s

    ans = 0
    t = 0
    for i in range(N):
        if t + A[i] > T:
            ans = i + 1
            break
        t += A[i]

    print(ans, t)

=======
Suggestion 6

def getSong(t, a):
    num = len(a)
    t = t % sum(a)
    for i in range(num):
        if t < a[i]:
            return i+1, t
        t -= a[i]
    return -1, -1

=======
Suggestion 7

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    t %= s
    for i, x in enumerate(a):
        if t < x:
            print(i + 1, t)
            break
        t -= x

=======
Suggestion 8

def main():
    N,T = map(int,input().split())
    A = list(map(int,input().split()))
    T = T%sum(A)
    for i in range(N):
        if T < A[i]:
            print(i+1,T)
            break
        else:
            T -= A[i]

=======
Suggestion 9

def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    t %= sum_a
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            break
        t -= a[i]
solve()

=======
Suggestion 10

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        if T <= A[i]:
            print(i + 1, T)
            break
        else:
            T -= A[i]
