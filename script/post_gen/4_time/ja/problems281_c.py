Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    t = 0
    for i in range(N):
        t += A[i]
        if t >= T:
            print(i+1, T-(t-A[i]))
            exit()
    T %= t
    t = 0
    for i in range(N):
        t += A[i]
        if t >= T:
            print(i+1, T-(t-A[i]))
            exit()

=======
Suggestion 2

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    T = T % total
    s = 0
    for i in range(N):
        if s <= T < s + A[i]:
            print(i + 1, T - s)
            break
        s += A[i]

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    t = t % a_sum
    a_sum = 0
    for i in range(n):
        a_sum += a[i]
        if t < a_sum:
            print(i + 1, t)
            break

=======
Suggestion 4

def main():
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    t%=s
    for i in range(n):
        if a[i]>t:
            print(i+1,t)
            return
        t-=a[i]
    return

=======
Suggestion 5

def problem281_c():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    print(t // sum(a) + 1, t % sum(a) + 1)

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if t % total == 0:
        print(n, total)
        return
    t %= total
    for i, ai in enumerate(a):
        if t > ai:
            t -= ai
        else:
            print(i+1, t)
            return

=======
Suggestion 7

def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    now = 0
    for i in range(n):
        if t < a[i]:
            ans = i + 1
            now = t
            break
        else:
            t -= a[i]
    else:
        ans = (t // sum(a)) * n + 1
        now = t % sum(a)

    print(ans, now)

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = A * 2

    s = 0
    for i in range(N):
        s += A[i]

    t = T % s
    if t == 0:
        t = s

    s = 0
    for i in range(N * 2):
        s += A[i]
        if s >= t:
            print(i + 1, t)
            break

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % T for a in A]
    A.sort()
    A.append(A[0] + T)

    i = 0
    while A[i] < T:
        i += 1
    print(i + 1, A[i] - T)

=======
Suggestion 10

def main():
    pass
